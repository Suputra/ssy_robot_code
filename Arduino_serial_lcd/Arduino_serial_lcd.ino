#include <Braccio.h>
#include <Servo.h>
#include <LiquidCrystal.h>

int commands[7] = {20, 90, 45, 180, 180, 90, 10}; //commands sent to robot 
String strCommand;
const int rs = 40, en = 41, d4 = 44, d5 = 45, d6 = 46, d7 = 47;

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup()
{
  Braccio.begin();
  lcd.begin(16, 2);
  lcd.print("Robot Start!");
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()) {
    strCommand = Serial.readStringUntil('\n');
    strCommand.trim();
    
    lcd.setCursor(0, 0);
    lcd.print(strCommand.substring(0, 11));

    lcd.setCursor(0, 1);
    lcd.print(strCommand.substring(11, 27));
    
    commands[0] = (strCommand.substring(0, 2)).toInt();
    
    for (int i = 0; i < 6; i++) {
      commands[i+1] = (strCommand.substring(4*i + 3, 4*i +7)).toInt();
    } 
  }
  Braccio.ServoMovement(commands[0], commands[1], commands[2], commands[3], commands[4], commands[5], commands[6]);
}
