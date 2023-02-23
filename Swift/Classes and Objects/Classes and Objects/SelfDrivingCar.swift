//
//  SelfDrivingCar.swift
//  Classes and Objects
//
//  Created by Isaac Hunter on 9/6/19.
//  Copyright © 2019 Isaac Hunter. All rights reserved.
//

import Foundation

class SelfDrivingCar : Car {
    
    var destination : String?  // called an optional, when use of var it must be called with a '!'
    
    override func drive() {
        super.drive()
        
//        if destination != nil {
//            print("driving towards " + destination!)  // unrap the optional - says that the var will not be nil. '!' means "manuel override"
//        }
        
        if let userSetDestination = destination {  // code only runs when destination is not nil
            print("driving towards " + userSetDestination)
        }
        
        
        
    }
    
}
