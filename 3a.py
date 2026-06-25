for hour in range(9,21):
    for minute in range(0,60,5):
        h_angle=(hour%12)*30+minute*0.5
        m_angle=minute*6
        angle=abs(h_angle-m_angle)
        if angle > 180:
            angle= 360 - angle
        print(f"{hour:02d}:{minute:02d}-{angle}degrees")
    print("................")
