/* 
 *  Author     : Wesley Cooke
 *  Date       : 04/01/2024
 *  Description: Elevator system using 3 push buttons with hardware debounce. 
 *               Tracks the state of the buttons being pushed and relays that 
 *               information over UART to the pi. 
 *               
 *               :TODO: Refactor movement methods. The main stepper motor driver
 *                      commands and polling functions can be refactored into 
 *                      a separate method. The moveElevatorUp and moveElevatorDown 
 *                      are two prime examples of this. 
 *                      
 *               :TODO: Refactor the checkButtons method. Functaionlity for the q
 *                      can be pulled out and an index for the floor can be passed. 
 *     
 *               
 */

// Button Pins
const int b0 = 13;
const int b1 = 12; 
const int b2 = 11;

// Motor Control Pins
const int pulse = 5; 
const int dir   = 6;
const int ena   = 7;

// Micro Switch Connections
const int botLimitSwitch = 3;
const int upLimitSiwtch  = 2; 

// How do we convert a step to a milimeter?
// The belt has a pitch of 2mm and the timing pully has 30 teeth. 
// This means that one full 360 degree rotation will move the gantry 30*2 = 60mm. 
// On the microstepper driver we have 200 steps set to to move the motor 360 degrees.
// The dimensional analysis is simple from here: 
// 200(steps/60mm) = 3.33 steps/mm.
float mmToSteps = 3.33;

// These are timing variables used to
// determine how long the elevator has been at a floor.
unsigned long visiting;
unsigned long state_sent; 

// These variables are for polling the states of the buttons. 
bool bs0;
bool bs1;
bool bs2;

// Queue Tracking variables 
int floors_requested[3] = {-1, -1, -1}; // The Queue for requested floors
bool already_requested[3];              // Keep track of its its alreayd in the Queue.  

int requested_num = 0;                  // num items in queue 
int req_p;                              // pointer for the floor to visit 
int current_step;                       // What step are we on? 
int floor_locations[3];                 // Will update based on limit switch values
int current_floor = -1;                 // -1 for not at a floor. 0, 1, 2 other wise. 

void moveElevatorUp(int numMM)
{
  int steps = numMM * (mmToSteps); // Convert the numMM to a set number of steps 

  // Set the direction to up and make sure elevator is enabled
  digitalWrite(dir, LOW);
  digitalWrite(ena, HIGH);
  // pulse for the required amount of steps
  for(int i=0; i<steps; i++)
  {
    // Continue polling our buttons and updating the queue and GUI. 
    checkButtons();
    printState();
    
    // If the upper limit switch is triggered, don't continue.
    // We have reached the top floor.  
    if (digitalRead(upLimitSiwtch) == HIGH)
    {
      digitalWrite(ena, LOW);
      digitalWrite(ena, HIGH);
      break; 
    }
    // Provide a pulse to the stepper motor driver. 
    digitalWrite(pulse, HIGH);
    delayMicroseconds(1000);
    digitalWrite(pulse, LOW);
    delayMicroseconds(1000);
  }
}

void moveElevatorDown(int numMM)
{
  
  int steps = numMM * (mmToSteps); // Convert numMM to a set number of steps

  // Set the direction to down 
  digitalWrite(dir, HIGH);
  digitalWrite(ena, HIGH);
  for(int i=0; i<steps; i++)
  {
    // Continue polling the buttons and updating the queue and GUI. 
    checkButtons();
    printState();
    // If the lower limit switch is trigered, don't continue.
    // We are at the bottom floor. 
    if (digitalRead(botLimitSwitch) == HIGH)
    {
      digitalWrite(ena, LOW);
      digitalWrite(ena, HIGH);
      break;
    }
    // Provide a pulse to the stepper motor. 
    digitalWrite(pulse, HIGH);
    delayMicroseconds(1000);
    digitalWrite(pulse, LOW);
    delayMicroseconds(1000);
  }
}

void goToLowerLimit()
{
  // Method to set the elevator to the lowest floor.

  // Set the direciton to down
  digitalWrite(dir, HIGH);
  digitalWrite(ena, HIGH);
  // Continue pulsing until we hit the lower limit switch. 
  while(digitalRead(botLimitSwitch) == LOW)
  {
    // Continue polling the buttons and updating the queue and GUI.  
    checkButtons();
    printState();
    digitalWrite(pulse, HIGH);
    delayMicroseconds(1000);
    digitalWrite(pulse, LOW);
    delayMicroseconds(1000);
  }
  // set the current step to 0
  current_step = 0;
}

void goToUpperLimit()
{
  // Method to set the elevator to the highest floor.

  // set the elevator to move up 
  digitalWrite(dir, LOW);
  digitalWrite(ena, HIGH);

  // Continue going up until the upper limit switch is hit. 
  while(digitalRead(upLimitSiwtch) == LOW)
  {
    // Continue polling the buttons and updating the queue and GUI. 
    checkButtons();
    printState();
    digitalWrite(pulse, HIGH);
    delayMicroseconds(1000);
    digitalWrite(pulse, LOW);
    delayMicroseconds(1000);
    // Increase the step number.
    current_step++;
  }
}

void setup() 
{
  // Set the buttons as inputs 
  pinMode(b0, INPUT);
  pinMode(b1, INPUT);
  pinMode(b2, INPUT); 

  // Set the motor control pins as outputs
  pinMode(pulse, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(ena, OUTPUT);

  // Start serial comms for the GUI. 
  Serial.begin(115200);

  // Calibrate the elevator
  goToLowerLimit();
  goToUpperLimit();

  // Set the first floor to be halfway between the upper and lower limits
  floor_locations[0] = 0;
  floor_locations[1] = current_step/2; 
  floor_locations[2] = current_step; 

  // Go back to the bottom floor
  goToLowerLimit();
  // Set the req_p to the beginning of the queue. 
  req_p = 0;
  current_floor = 0; 
}

void checkButtons()
{
  // This method must be polled to ensure the button presses are responded to

  // Read the buttons.
  bs0 = digitalRead(b0);
  bs1 = digitalRead(b1);
  bs2 = digitalRead(b2);

  // If the bottom floor button has been pressed. 
  if (bs0)
  {
    // If our queue isn't full and this floor isn't already in the queue
    if (requested_num != 3 and already_requested[0] != 1)
    {
      // If the current pointer for the queue is open, 
      // place the floor there. 
      if(floors_requested[req_p] == -1)
      {
        floors_requested[req_p] = 0;
      }
      // If the next pointer for the queue is open, place it there
      else if(floors_requested[(req_p+1)%3] == -1)
      {
        floors_requested[(req_p+1)%3] = 0; 
      }
      else // If the final pointer for the queue is open, place it there
      {
        floors_requested[(req_p+2)%3] = 0; 
      }
      // Increment the number of items in the queue. 
      // Set this floor as already having been added. 
      requested_num += 1;
      already_requested[0] = 1;
    }
  }
  // The comments are carbon copies of the above. The inner functionality 
  // should be made a function call, passing in the floor number. Hence the :TODO:
  if (bs1)
  {
    if (requested_num != 3 and already_requested[1] != 1)
    {
      if(floors_requested[req_p] == -1)
      {
        floors_requested[req_p] = 1;
      }
      else if(floors_requested[(req_p+1)%3] == -1)
      {
        floors_requested[(req_p+1)%3] = 1; 
      }
      else 
      {
        floors_requested[(req_p+2)%3] = 1; 
      }
      requested_num += 1;
      already_requested[1] = 1;
    }
  }
  if (bs2)
  {
    if (requested_num != 3 and already_requested[2] != 1)
    {
      if(floors_requested[req_p] == -1)
      {
        floors_requested[req_p] = 2;
      }
      else if(floors_requested[(req_p+1)%3] == -1)
      {
        floors_requested[(req_p+1)%3] = 2; 
      }
      else 
      {
        floors_requested[(req_p+2)%3] = 2; 
      }
      requested_num += 1;
      already_requested[2] = 1;
    }
  }
}

void loop() 
{
  // Continue polling the buttons and updating the queue and GUI.
  checkButtons(); 
  printState();

  // Get the floor we shoud visit next. 
  int floor_to_visit = floors_requested[req_p];

  // If it's the bottom floor 
  if (floor_to_visit == 0)
  {
    // Go to the bottom and set the current floor
    goToLowerLimit();
    current_floor = 0;

    // Stay for 2 seconds
    visiting = millis(); 
    while((millis() - visiting)< 2000)
    {
      // Continue polling the buttons and updating the queue and GUI.
      checkButtons();
      printState();
    }

    // Take this item out of the queue and reset it's tracking variables.
    // Increment the queue pointer. 
    already_requested[0] = 0;
    floors_requested[req_p] = -1;
    req_p = (req_p + 1)%3;
    requested_num--;
    // Set the current step number. 
    current_step = 0;
  }
  // If it's the top floor 
  if (floor_to_visit == 2)
  {
    // Go to the top and set the current floor. 
    goToUpperLimit();
    current_floor = 2;
    
    // Stay for 2 seconds 
    visiting = millis(); 
    while((millis() - visiting)< 2000)
    {
      // Continue polling the buttons and updating the queue and GUI.
      checkButtons();
      printState();
    }

    // Take the floor out of the queue and reset it's tracking variables. 
    already_requested[2] = 0;
    floors_requested[req_p] = -1;
    req_p = (req_p + 1)%3;
    requested_num--;
    // set the current step from calibration. 
    current_step = floor_locations[2];
  }

  // If it's the middle floor 
  if (floor_to_visit == 1)
  {
    // Are we above? 
    if(current_step > floor_locations[1])
    {
      // Move elevator down
      moveElevatorDown((current_step - floor_locations[1])/mmToSteps); 
      
    }
    // are we are below?
    else if (current_step < floor_locations[1])
    {
      // Move elevator up 
      moveElevatorUp((floor_locations[1] - current_step)/mmToSteps); 
    }

    current_floor = 1;
    visiting = millis(); 
    while((millis() - visiting)< 2000)
    {
      // Continue polling the buttons and updating the queue and GUI.
      checkButtons();
      printState();
    }
    // Reset this floor
    already_requested[1] = 0;
    floors_requested[req_p] = -1;
    req_p = (req_p + 1)%3;
    requested_num--;
    current_step = floor_locations[1];
  }
}

void printState()
{
  // This method uses a software debounce so we aren't 
  // sending data over too frequently. 
  // Get the current time
  unsigned long current = millis();

  // If we haven't sent something in the past 0.5 seconds. 
  if((current - state_sent) > 500)
  {
    // Send our data over with a starting byte and end byte. 
    Serial.println("S");
    Serial.println(floors_requested[0]);
    Serial.println(floors_requested[1]); 
    Serial.println(floors_requested[2]);
    Serial.println(current_floor); 
    Serial.println("E");
    // remeber that we just sent something. 
    state_sent = current;
  }
}
