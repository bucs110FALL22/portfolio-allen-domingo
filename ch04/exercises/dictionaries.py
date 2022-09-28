article = "In case the U.S. economy wasn't hurting enough already, the Federal Reserve has a message for Americans: It's about to get much more painful. Fed Chair Jerome Powell made that amply clear last week when the central bank projected its benchmark rate hitting 4.4% by the end of the year — even if it causes a recession. There will very likely be some softening of labor market conditions Powell said in his September 21 economic outlook. We will keep at it until we are confident the job is done."

switch = {
  "Its":"awesome",
  "projected":"doomed to fail",
  "will":"possibly",
  "labor":"farmer's",
  ".":", mhmm."
}

for key, value in switch.items():
  article = article.replace(key,value)


print(article)