import random
import golf_config as gc
import golf_kafka as gk
import uuid
import json

if __name__ == "__main__":
            
    # Assign temporary scorecard for each golfer
    golfer_strokes = {name: (1, 0) for name in gc.golfer_names}

    for hole, (par, distance) in gc.course_yardages.items():

        # Ensure each golfer has an empty scorecard for each hole
        # golfer_strokes = {golfer: (1, 0) for golfer in golfer_strokes}

        for golfer in golfer_strokes:

            stroke, yards = golfer_strokes[golfer]
            
            # Simulate until the golfer either gets the ball in the hole or hits triple bogey
            while yards < distance and (stroke - par <= 3):

                # Gather simulated data
                simulation = gc.simulate_hole(stroke, par, yards, distance)
                yards = min(simulation[0], distance) 
                club = simulation[1]

                # Put it in a raw message and send to Kafka topic
                message = json.dumps({
                    "Record":str(uuid.uuid4()),
                    "Hole":hole,
                    "Golfer":golfer,
                    "Stroke":stroke,
                    "Par":par,
                    "Yards_To_Pin":yards,
                    "Pin_Distance":distance,
                    "Club":club}).encode('utf-8')
                # gk.send_message_to_topic(message, f"scorecard_{golfer.lower()}")
                print(message)

                stroke += 1

