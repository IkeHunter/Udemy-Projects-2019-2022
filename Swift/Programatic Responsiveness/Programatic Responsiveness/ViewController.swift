//
//  ViewController.swift
//  Programatic Responsiveness
//
//  Created by Isaac Hunter on 8/15/19.
//  Copyright © 2019 Isaac Hunter. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let square = UIView(frame: CGRect(x: self.view.frame.width/2 - 50, y: self.view.frame.height/2 - 50, width: 100, height: 100))
        square.backgroundColor = UIColor.red
        self.view.addSubview(square)
        
        /*
         x = self.view.frame.width == max width of device
         y = self.view.frame.height == max height of device
         */
        
    }


}

