# 中文情感分析与可视化 -- 2021
# Sentiment Analysis and Visualization Based on Chinese Text

## Abstract   
As the Internet developed in a rapid trend, there are many social applications in the 
market, as well as shopping, takeout, and reservation software, such as Taobao, Ele.me, 
Meituan, etc. There are a lot of comments in these applications, sometimes there are even 
thousands of them. If we can use these data as efficiently as possible, we can quickly analyze 
and process public opinions, and provide help for market analysis and other applications. 
This kind of data is often very large in scale, if only rely on manual reading and analysis, it 
must cost a bunch of time and energy, and the accuracy can not be well guaranteed. How to 
use the Natural Language Process method to effectively obtain and analyze public opinion 
in the massive text data has become a very practical problem.   

The mainstream research direction was based on supervised learning, especially Deep 
Learning for Text Sentiment Analysis. Convolutional Neural Network (CNN) and Long-term 
and Short-term Memory Network (LSTM) were two kinds of Deep Learning Network 
Models used in the field of Natural Language Process. Using the LSTM model, we could 
train a three-level classifier for emotional analysis with positive, neutral, and negative, and 
input it as a sequence of sentences. For the major parts of the evaluation information, there 
are three typical emotions: positive, negative, and neutral, so we can train a model with good 
prediction ability.   

In this project, we use the Keras to build a Neural Network model. For text sentiment 
analysis, we need to consider the importance of text sequence and sentiment features. This 
biLSTM model consists of four layers. The first layer is the embedding layer, to reduce the 
dimensions of the neural network; the biLSTM layer is the second, and its second dimension 
is a sequence. For 32 units, 64 units are set because of using bidirectional LSTM; the third 
layer is the biLSTM layer to import the returned sequence a One-way LSTM, and return a 
result; the last layer is the full connection layer, to input a value from sigmoid, and judge 
whether the input text is a positive emotion or negative emotion.   

In the aspect of visualization, Pyqt5 is used to design GUI. Pyqt5 is developed by Python 
3.8, and the interface of the button and label provided by pyqt5 is used. When creating a new 
window, Widget is used for development; PushButton is used for a button, and its size, text, 
and other attributes are set; Label is used as an input text box for sentiment analysis, and 
adjusts the font color, size; the final output results, based on the output results of three 
categories, are transfered into positive evaluation, negative evaluation, and neutral 
evaluation.   

In this paper, a visual tool is made for the emotional analysis model, which allows users 
to customize the text of the test, click the 'forecast' button to predict emotion, which 
simplifies the difficulty of using it. The visualization tool uses the corresponding method to 
realize the switching of multiple windows and calls the Chinese emotion analysis project to 
run and return the results in the window.   

** Key words：Chinese Text Sentiment Analysis; biLSTM; CNN; Text Sentiment 
Visualization **
