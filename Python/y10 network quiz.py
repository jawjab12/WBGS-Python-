#**********************************************************************************
#QUIZ ON NETWORKS
#***************************************************************************************

import time
score = 0
total_questions = 5

print("TCP/IP Protocol Quiz")
time.sleep (0.5)
print("Type the TCP/IP layer for each protocol.")
time.sleep (0.5)
print("Valid layers: Application, Transport, Internet, Link")
layers = {
"TCP": "TRANSPORT",
"UDP": "TRANSPORT",
"IP": "INTERNET",
"HTTP": "APPLICATION",
"HTTPS": "APPLICATION",
"SMTP": "APPLICATION",
"IMAP": "APPLICATION",
"ETHERNET": "LINK",
"WI-FI": "LINK"
}
    for i in range (total_questions):

        print("\nQuestion", i + 1, "of", total_questions)
        protocol = input("Protocol (e.g., TCP, IP, HTTP, SMTP): ").strip().upper()
        print("Protocol:", protocol.title())

    print("Protocol:", protocol.title())
    answer = input("Layer: ").strip().upper()
    if protocol not in layers:
        print("Unknown protocol - check spelling. No point this round.")

    correct = layers[protocol]
    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print("Not quite.")
        print("Correct layer was:", correct.title())
        print("Final score:", score, "/", total_questions)

