def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 255)
    else:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 255)
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 0)
                maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 255)
        else:
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
                maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
                maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
                    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
                    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
                else:
                    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
basic.forever(on_forever)
