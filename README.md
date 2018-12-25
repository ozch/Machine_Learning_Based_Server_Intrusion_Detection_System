# Anomaly_Detection_Models_Creation
<h2> if you're here. you know what you want. So you can figure it out your self :) </h2>

# Dataset
  <p>NSL KDD Intrusion Detection Dataset <emp>(it's kddcup99 on steroids)</emp></p>

# How to Run
  <p>1. Build and run feature_extractor for real time feature collection (it'll automaically start feeding data to python program using ZMQ)</p>
  <p>2. Run main_flood.py for DDoS detection (feature_extractor must be running in background)</p>
  <p>3. Run main_ssh.py for ssh attack detection (only works on linux server,you might have to change auth.log location in main_ssh.py file)</p>
  <p>4. All files start with nsl.*.py are model retraining,this program automactically collects and labels data for improve model (self_learning) with admin feedback, run these file to calliberate model according to your network<emp>(require atleast 6 days of training,i mean program actively running)</emp>, you can automate this process(but i'm done for now)</p>
  <p>5. Was working on fishing attack but got tired,because it's client side attack</p>
  
# Papers:
<pre>
     1. Martina Troesch, Ian Walsh, Machine Learning for Network Intrusion Detection.pdf
     2. Network Intrusion Detection Using Machine Learning .pdf
     3. Toward Generating New ID Dataset and Intrusion Trafﬁc .pdf
     4. NSL-KDD99 (Doc from the some offical website)
     5. A Study on NSL KDD Dataset for IDS.pdf
     6. A Detailed Analysis of the KDD CUP 99 Data Set.pdf
     7. Feature Extraction Mehtod for IDS.pdf  
</pre>
