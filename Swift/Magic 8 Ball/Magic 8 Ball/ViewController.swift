//
//  ViewController.swift
//  Magic 8 Ball
//
//  Created by Isaac Hunter on 7/30/19.
//  Copyright © 2019 Isaac Hunter. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var ballView: UIImageView!
    
    var ballIndex : Int = 0
    
    let ballImages = ["ball1", "ball2", "ball3", "ball4", "ball5"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        ballChange()
    }

    @IBAction func askButton(_ sender: UIButton) {
        ballChange()
    }
    
    func ballChange(){
        ballIndex = Int(arc4random_uniform(5))
        
        ballView.image = UIImage(named: ballImages[ballIndex])
    }
    
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        ballChange()
    }
    
}

