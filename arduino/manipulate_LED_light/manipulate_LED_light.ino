#define LED_WARM_PIN 3 //теплый свет
#define LED_COLD_PIN 5 //холодный свет
#define LIGHT_SENSOR 0 //световой сенсор
#define POT A0 //Вход потенциометра

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  pinMode(LED_WARM_PIN, OUTPUT);
  pinMode(POT, INPUT);
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void setupLEDvalue(int outputValueLED, int inputValueLED) {
   //считываем управляющее значение
   outputValueLED = map(inputValueLED, 0, 1024, 0, 255);
   
   //записываем уровень яркости
   analogWrite(LED_WARM_PIN, outputValueLED);
}

//функция определения команды. Должна дальше отослать параметры

void loop() {
  String arduinoOperation = "";
  
  if (stringComplete) {
    Serial.print("You say: ");
    Serial.println(inputString);
    
    char charBuf[32];
    inputString.toCharArray(charBuf, 32);
    char * pch = strtok (charBuf, " ");
    
    Serial.println("Ard say: ");
    while (pch!=NULL){
      Serial.println(pch);
      pch = strtok(NULL, " ");
    }
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
