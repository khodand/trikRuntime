# Copyright 2019 CyberTech Labs Ltd. & Andrei Khodko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import types

script = types.SimpleNamespace()
script.random = script_cpp.random
script.wait = script_cpp.wait
script.time = script_cpp.time
script.timer = script_cpp.timer
script.system = script_cpp.system
script.writeToFile = script_cpp.writeToFile
script.writeData = script_cpp.writeData
script.readAll = script_cpp.readAll
script.removeFile = script_cpp.removeFile
script.run = script_cpp.run
script.quit = script_cpp.quit
script.reset = script_cpp.reset
script.getPhoto = script_cpp.getPhoto

class KeysEnum():
    Left = 105
    Up = 103
    Down = 108
    Enter = 28
    Right = 106
    Power = 116
    Esc = 1

class Events():
    Sync = 0
    Key = 1
    Relative = 2
    Absolute = 3
    Misc = 4

class MouseEventCodes():
    X = 0
    Y = 1
    Wheel = 8

    LeftBtn = 272
    RightBtn = 273
    MiddleBtn = 274

class PadEventCodes():
    BtnA = 304
    BtnB = 305
    BtnC = 306
    BtnX = 307
    BtnY = 308
    BtnZ = 309

    BtnTL = 310
    BtnTR = 311
    BtnTL2 = 312
    BtnTR2 = 313
    BtnSelect = 314
    BtnStart = 315

    X = 0
    Y = 1
    Z = 2
    Rx = 3
    Ry = 4
    Rz = 5

    Throttle = 6
    Rudder = 7
    Wheel = 8
    Gas = 9
    Break = 10

    Hat0X = 16
    Hat0Y = 17
    Hat1X = 18
    Hat1Y = 19

aliases = ["A1", "A2", "A3", "A4", "A5", "A6", "T1", "T2", "T3", "W1", "W2", "W3", "W4"
        , "D1", "D2", "D3", "F1"
        , "M1", "M2", "M3", "M4"
        , "B1", "B2", "B3", "B4"
        , "E1", "E2", "E3", "E4"
        , "C1", "C2", "C3"
        , "SS1", "SS2", "SS3", "SS4", "SS5", "SS6", "SS7", "SS8", "SS9", "SS10", "SS11", "SS12", "SS13", "SS14"
        , "U1_0x11", "U1_0x12", "U1_0x13", "U1_0x14", "U1_0x15", "U1_0x16", "U1_0x17", "U1_0x18", "U1_0x19", "U1_0x1A", "U1_0x1B", "U1_0x1C", "U1_0x1D", "U1_0x1E", "U1_0x1F", "U1_0x20"
        , "U2_0x11", "U2_0x12", "U2_0x13", "U2_0x14", "U2_0x15", "U2_0x16", "U2_0x17", "U2_0x18", "U2_0x19", "U2_0x1A", "U2_0x1B", "U2_0x1C", "U2_0x1D", "U2_0x1E", "U2_0x1F", "U2_0x20"
        , "U3_0x11", "U3_0x12", "U3_0x13", "U3_0x14", "U3_0x15", "U3_0x16", "U3_0x17", "U3_0x18", "U3_0x19", "U3_0x1A", "U3_0x1B", "U3_0x1C", "U3_0x1D", "U3_0x1E", "U3_0x1F", "U3_0x20"
        , "U4_0x11", "U4_0x12", "U4_0x13", "U4_0x14", "U4_0x15", "U4_0x16", "U4_0x17", "U4_0x18", "U4_0x19", "U4_0x1A", "U4_0x1B", "U4_0x1C", "U4_0x1D", "U4_0x1E", "U4_0x1F", "U4_0x20"
        , "U5_0x11", "U5_0x12", "U5_0x13", "U5_0x14", "U5_0x15", "U5_0x16", "U5_0x17", "U5_0x18", "U5_0x19", "U5_0x1A", "U5_0x1B", "U5_0x1C", "U5_0x1D", "U5_0x1E", "U5_0x1F", "U5_0x20"
        , "U6_0x11", "U6_0x12", "U6_0x13", "U6_0x14", "U6_0x15", "U6_0x16", "U6_0x17", "U6_0x18", "U6_0x19", "U6_0x1A", "U6_0x1B", "U6_0x1C", "U6_0x1D", "U6_0x1E", "U6_0x1F", "U6_0x20"
        , "U7_0x11", "U7_0x12", "U7_0x13", "U7_0x14", "U7_0x15", "U7_0x16", "U7_0x17", "U7_0x18", "U7_0x19", "U7_0x1A", "U7_0x1B", "U7_0x1C", "U7_0x1D", "U7_0x1E", "U7_0x1F", "U7_0x20"
        , "TEMP_DHT11_1", "TEMP_DHT11_2", "TEMP_DHT11_3", "TEMP_DHT11_4", "TEMP_DHT11_5", "TEMP_DHT11_6", "TEMP_DHT11_7"
        , "TEMP_DHT11_8", "TEMP_DHT11_9", "TEMP_DHT11_10", "TEMP_DHT11_11", "TEMP_DHT11_12", "TEMP_DHT11_13", "TEMP_DHT11_14"
        , "TEMP_DHT22_1", "TEMP_DHT22_2", "TEMP_DHT22_3", "TEMP_DHT22_4", "TEMP_DHT22_5", "TEMP_DHT22_6", "TEMP_DHT22_7"
        , "TEMP_DHT22_8", "TEMP_DHT22_9", "TEMP_DHT22_10", "TEMP_DHT22_11", "TEMP_DHT22_12", "TEMP_DHT22_13", "TEMP_DHT22_14"
        , "HUM_DHT11_1", "HUM_DHT11_2", "HUM_DHT11_3", "HUM_DHT11_4", "HUM_DHT11_5", "HUM_DHT11_6", "HUM_DHT11_7"
        , "HUM_DHT11_8", "HUM_DHT11_9", "HUM_DHT11_10", "HUM_DHT11_11", "HUM_DHT11_12", "HUM_DHT11_13", "HUM_DHT11_14"
        , "HUM_DHT22_1", "HUM_DHT22_2", "HUM_DHT22_3", "HUM_DHT22_4", "HUM_DHT22_5", "HUM_DHT22_6", "HUM_DHT22_7"
        , "HUM_DHT22_8", "HUM_DHT22_9", "HUM_DHT22_10", "HUM_DHT22_11", "HUM_DHT22_12", "HUM_DHT22_13", "HUM_DHT22_14"
        , "S1", "S2", "S3", "S4", "S5", "S6"
        , "video1", "video2"]

for i in aliases:
  globals()[i]=i

gamepad = brick.gamepad()
getPhoto = script.getPhoto
