# Serverless-Architecture
1. [Load Balancer Health Checker](#load-balancer-health-checker)
2. [EC2 Backup To S3 Bucket](#ec2-backup-to-s3-bucket)
   
---
### Load Balancer Health Checker
#### Steps To Replicate

1. Login to AWS Console search Lambda.
  > ![image](https://github.com/patilajayv/Serverless-Architecture/blob/main/SearchLambda.png)


2. Click on Create function
  > ![image](https://github.com/patilajayv/Serverless-Architecture/blob/main/createLambdaFuction.png)
   
   
3. Fill Details as per Image and click on Create Function
  > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/detailsLambda.png)
  

4. Add code which is mention in file [loadBalancerHealthChecker.py](https://github.com/patilajayv/Serverless-Architecture/blob/main/loadBalancerHealthChecker.py)
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/codeLambda.png)

5. Set Up cloudwatch Eventbridge add create Rule and Set parameter as per the image
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/CW_1.png)
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/CW_2.png)
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/CW_3.png)
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/CW_4.png)
   
   
6. Check mail alert
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/mailNotification.png)


 ---
 ### EC2 Backup To S3 Bucket
#### Steps To Replicate

1. Login to AWS Console and Create S3 Bucket as per images
   > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/S3_1.png)
   > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/S3_2.png)
   > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/S3_3.png)
2. Click on Create function
  > ![image](https://github.com/patilajayv/Serverless-Architecture/blob/main/createLambdaFuction.png)
   
   
3. Fill Details as per Image and click on Create Function
  > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/detailsLambda.png)
  

4. Add code which is mention in file [ec2Bkp.py](https://github.com/patilajayv/Serverless-Architecture/blob/main/ec2Bkp.py)
 > ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/codeLambda.png)


5. Click on add trigger and fill details according to image and click on add
> ![GitHub Logo](https://github.com/patilajayv/Serverless-Architecture/blob/main/Env_trigge_rule.png)
   



