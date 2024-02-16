# Container Fill Level Measurement

In this project, a PCB circuit and software compatible with Raspberry Pi 3B+ have been designed to measure the fill level of the container using an acoustic distance sensor and display it on an LCD screen.
The following hardware components are utilized:
- HC-SR04 Sensor: It has been used for distance measurement.
- 2x16 LCD Display: It has been used for displaying results.
- I2C LCD Adapter Board: A device has enabled the connection of a 16-pin LCD screen to the Raspberry Pi using only 4 pins.
- Buzzer: It serves the function of an alarm.
- Button: It is used to initiate measurement and reset the measurement.

To enable the use of the I2C converter, the I2C connection has been activated through the Raspberry Pi configuration screen.
The necessary library for the LCD screen has been installed.
When the program is executed, it opens on the screen with the message "Derinlik Ölçümü İçin Butona Basın" Upon pressing the button, the initial measurement is taken and considered as the depth of the empty container, which is then displayed on the LCD screen. Subsequent measurements determine the fill level of the container and continue to be displayed on the screen. Pressing the button again restarts the program.

Circuit Diagram:

![4](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/02ecf261-6d41-4f40-aed5-17807758a56f)
![5](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/94775de4-aae2-4476-a666-bea4fd4ee416)

Final State of the Project:

![6](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/31520b56-d2d9-46af-b2e9-abf3cac14466)
![7](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/7af0f202-9414-4922-b2b3-861fec927141)
![8](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/48d471ca-4041-4978-b885-57bb6f10e544)
![9](https://github.com/anilordu/Container-Fill-Level-Measurement/assets/120724452/e9aa1ee9-1ed7-49df-9f52-f7042ae69c9b)


