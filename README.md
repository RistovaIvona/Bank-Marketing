<!DOCTYPE html>
<html>
 <head>
 </head>
<body>

<h2>Bank Marketing (with social/economic context)</h2>

<h3>Introduction </h3>

<small><p>
 <i>"Data-driven marketing is the engine behind improved marketing results and it creates measurable internal accountability as marketers become more effective in planning, executing and proving the value of their work" - Lisa Arthur </i>
 
Over the past decade, information consumption has drastically shot up, generating million terabytes of data every single day. For marketers, this amount of data is a gold mine. If this data could be properly processed and analyzed, it can deliver valuable insights. Data Science is a field that extracts meaningful information from data and helps marketers in discerning the right insights.These insights can be on various marketing aspects such as customer intent, experience, behavior, etc that would help them in efficiently optimizing their marketing strategies and derive maximum revenue.</p>

<p>This project is about marketing campaign of Portuguese bank for term deposits with data of contacted customers in period of 2008 to 2010 and their respond of the calls. The data has 41188 observations of calls with 20 customer’s demographic and transaction features each. Analyzing the customers’ features in correlation with their responses of the calls should lead to identify type of customers which are more likely to make term deposits.

The aim of the project is to build a model which will predict the future response of new targeted customer.
The project is done in few phases:
<ol>
 <li>Data Cleaning</li>
 <li>Features Analysis and Visualization</li>
 <li>Models implementation</li>
 <li>Models Summary</li>
 <li>Conclusion</li>
</ol>
 
</small></p>

<h3>Data Cleaning</h3>

<p>There is no missing or incomplete values. All data left by clients as inaccessible/incomplete are attached as unknown.
The purpose of our analysis is not to delete the missing data, but to find a correlation between the data and thus fill it.
It is important to note that the unknown values in all features are not more than 5%. Considering this, we can use the correlation for fillment the 'unknown' values.
In the part of outliers, because it is about personal information and we do not have values that are unrealistic, they remain as specific cases. An example in this part are clients with more than 80 years that should not be deleted from the dataset.</p>

<h3>Features Analysis and Visualization</h3>

<img src="https://pasteboard.co/JjpHyvY.png">

<p> Dataset has unbalanced standard distribution ("Yes" - 12% and "No" - 88%). 
 
<img src="https://lh3.googleusercontent.com/kQOk3kO3TaXw3RUZ6oeCnOQggo5shQMAjrvmfcixJ_dpb5NDWT7-5SJtfbGqrdWO6xddQfhYPsJcYsdmnWe9w_LLH7w3nFrkXZh1qM1zJ0d5yqBLGVIHIGEisJ3GBUsAHgfZ5cyAJGmZTQ0c8SGjxIGbXkAtqW3zCbw3jPk0X2R1LgxnMMu0mZ5lzCVsc9bbSdkuU7Rq3gIqVDKShMgYiVPKEpbT9_DzEsL39rYzI8zK2GiLyD95Xy8US8Ji9ouBtJD6LrBISkvXLnDtYzSQ8zDgoXHmfSNIftffOZ3PJDW8WGHzZ6WA88DvrEAWy7HCGjapdk_DhnKw5xaO-25Dg74VLA-VMVV1bsPEkjdLH-neWfVDsV6Q5vUXXrLmi9wh50QXwMSkGWIAB-gWAC9NTw1ZsrnmuCnhWEjCefh9QzWshwKUjbkl3yR7WeAM2lepxx4IXY_JA3VzP4hWR58WHGemB7P1y9MREUJJ1gKvfK7CRer5mq-oUSxZxKi0D9MSukflF01u5zdxA5WcbbN6SDUfD1JmWAymbepRbqHcgIJ9H89wwE5ZgVxVTMlQZQntXk_kM3-uFU2fue_SOuRHDDZ6C-SAvK0qdEz15XiGSTdDAmECXzz42SNfC1Pmdhq2kC9szmvJHzkOZHfxSt1HNOMXSjN9Nqo5DRW46mLSDOT0BvFoZH9xoZ6hhCcOl3Vs8xmtWg=w1920-h942-ft">

<img src="https://lh3.googleusercontent.com/yOVw_MAEiEOk-jhDRqZNaDAOXT-zjzwUvzZi2_NgBRMW22pMSonfCl4wSkZ9wNFqFFTC998eHfsykBZ1ZEBoByOYhU4r2jdSudq4UD2CK1aBQKquYjfdO68J2DkGwfLyrEn41OTk4zzN-NrYBztcJm7ppR3lkW6Lbay5O1Zs2zGjOwfU-FW9Av16Fvg9Tp668oyW3TaApyHh-bQwI5FFfwT40UDkIv19g-iDCREnKxcg87semo6j3tHOiHh585fPxsyy3hkWbDB8yc2Ncpc983pJiYZre-xcZDRgZ59l43Ti7K68Z2wSv4Ogs7mpbO-v8yX47ZuqxSg9HgrHq9-xt9Vd0ds1ZBHrApuqMeqw0jaF-gezo2I1zB98NKKX97CmZbYjP1DCDOIAJ1d43BDLj1FgP9Agy4DcWMY5CMfHq6GzOpZ8ZeNmgXZHEzP1VQNzVW3sM-RAmPGl2bSjgaKpTYAFZDH_QnIVDKcnLBiTBPg1YyIQrHtccHCR3zQnNGom24JbgfFnlxjpjdD7JayFicnH0GODdRfCYkR9IFz6zJReknUUyHrWPIr2RytiJUue0s5WBfW641oKMJnJV-dcox-_Gs9tK8G1hma-TPF-wH4b19RiG5c_49mFDg4Gb4eP8vhJgL1_EQx6_5cTpb4jNleH6RQOv3QPkRShSrkkqrFB_NKzdNESOD0egjeLEtsAAwoSiA=w1920-h942-ft">
 
<p>The majority of the costumers belong into group from 30 to 40 years. Considering the distribution of the class and the age-variable, we divided the customer in the different age-groups in order to make better analysis how age influance on the subscription rate. 
The bank was more effective with 20s and 60s aged group, which should be the next target. Considering that the term deposits are the most liquid and the most secure investment, the pattern is expected.The oldest aged group want to have cash and youngest do not have experience, knowledge and enough money for better and more sophisticated investments. On other hand, the 30s aged group have more loans and less money for savings.</p>

<img src="https://lh3.googleusercontent.com/DF70y9pERzAKVCcsn8_WdMdzswvdRPFBJXz-jDnEjNW60P3bQO3iITn5OqX_RplmsdX3L1MyAtuRVB2-e9GhNmzjbzGdduK3lmMaCrKdNRAclMnkaOwOAAHi1P1y8K2zT6L10fcIwlRFFpUOi-9HgWF3COWwJqQXHgJQp_uUF1lXxbDH442pbsqDmaFQcL2js4I21spDIFD3nOi5GHK8ZNsmqsS36t1oNv4Tk2fzxzW2b6YtnnKYQlX8x6aKWCNdRraOfushDekFMXTQWedqJdjIswa9V96P5dz57tQ-wBA68_P_djeaws0WdxsE1a66i-fydKAb2pLcv3r6RAqKgjBcUxzbGF2XSG9cs2y3uB8IcM9jtymVBTwqdB0pNyDlyFosp1wMw4H5UnYqrRVub1WY5xuEU41DOawSKPi2boB_-BwYlNwwNwG6NXbQKX5oDVWsEZjWeqNFK6PrWnjTioN-zjCEks-FAh4DAnxDWgm4QdKtoznxYINRjV_ZTPK12gDZRlkRssrHKnNbdshu6LzcAHzawCvuPRU7Zs5zauz0d2PNpPxuijV-SBplCw4Mxv7-Ef45nQEjLzjQyfON9sRC1zSUPTLiNuJZ65Nn2Xr18vvVVFpjypeo9xiDn8VsGg0kOHjaC7vRp-69KV_JzoZplppKubRmS2X1va_URFb-uEi-Ht2wp02CcQElVcsFhBsD7w=w1920-h942-ft"> 

<p> Also the "duration" (last contact duration) can be useful feature for predicting the target variable. It is expected because it is already mentioned in the data overview that this field highely affects the target variable and should only be used for benchmark purposes.</p>

<img src="https://lh3.googleusercontent.com/wGTZGIYIaFlyueJ9lpLKAJlCzswqLwItatSyY2HqAN5OlDj-9zpHP8hB1vaf16m43Foot7m6ZNy3lyuzGPBFu2lElVOhpHcxnrFhuPULRykMdy-nEsSDMsN6bOy7suv7TJtgIR2GK3LmsRvuBW4J726O6fHMDe-gTJBjrKnbee7tIPx6KXVYRkZJcS-4L3K7AfE8kcaFWUY6zfJFhaqzEvtfoyn0qtDqEu5hh-vaSVy6gjQsC7nHmEaiKb-uhpMk41BTxKz9J9fSvzbqFfWFviKfZOoryoWcNEruuYD5ZNj-sFP7vBq2lpLqjMLKIlii7_HAUgOL-rQDjgDTc79vu3EKSC-DfqJIVN3581JJWbj9NhNzsQVnd5qOZc1S0LDVf0cjsyCs38afHf7_4sGrRgR0dUxMR73PyjMgEhzMEPfGh9tY9_lf6pQwUvGxXyMnMp5tot9C9W8taxaeQc67M675tmcDvvXqLddL_urV-URRCQTN86lBP8CCghIp0wMBdje_-kh0hm8_C_noE8cZGRq87s1e4E5-bZxcLCfu8nXHmEUTWfcjjXZCRwPkAYRyDcYmp4EMBolLl1XMi8GgvnvBRcOB7XWqheLm3fkJlYFhdkXRwYWDo6Oa9bSyGOXf7f_jDGkqRRu8iMdsAWK_kiMzFgitQ6K6cARjpIuypsCASpl92On3hWyebJADDz-_BdJyOA=w1920-h942-ft">
<img src="https://lh3.googleusercontent.com/nUhcpDCGR2YVgG7AMELy2GXAQ-7jcA5DBTaybbToXpM4OERY6B-I0VOoAy3ZpfHPPw6TAZP9zEnN6dsu_4kvi54tBvSh-0RJoYwXPc2lXBONBP87SZ16g97pabiokuGMKiVF1k3RRWVr85MbsTtDCPEt9hWbwXAZe_ixTRUGHYzlWN8GM-57lnAkvzrrGRZ5n9VmwOvOj5ko3NT-TR3pMQgqsD8E9g_jSlCU4dKiCDc24QHMF-7a4uhUuUR1-R8UJJ56R98NKwPscCRJ5_h8luPzFmjxW4R9ewceZdtXqrba5D8LwCumdopROfdNY5Y8640FRsU8OWQ_Wu_nisvhdgMGDEAThP5reIesEzCoiBz2PC-JhWexjePebxWTSfyq_EOjqOuyEJLUinvOHU4Ty-fyTgLwWI5kFg_0Q8l76ngRxDRHSl_cncqvsZ9dgGHTEECCFHB7Lg6xFzVQpztusvEVtnkHle2hZHcSgYybZxqy8e3PYj_g7_IWA12tSUYXo1gMB5pHWueaGJ7qbng5RS08rIKl9ImAvQDZ5UIzQ6XBr8M_sFfx_lCNzyW88nb9ZH7uKeFfjciQVrlo7UY7QcxGz3KXHU56F_oFrTsGe4h90QCiCXZx9IlbWP5h2PzGBHjG5pg2bHtHjkb5Xn-pUFeGX5olQq1nh97mQVRu7UfGhBc65fy-Do4gQ1cSKk1ef0D88Q=w1920-h942-ft">
<img src="https://lh3.googleusercontent.com/ciM7Z4Cc0jeb3Fa9nq3HLN6kKnSNzttjn318HAxLEUbKiSwkcUSHwRabB0E1KcIVCWzdaNiZnwZamxJ50fjZ1JN3wMaDXmXC_kx5chQz8G9hdSdUJPbEdyHx4YohjTxmtFVG_oOfwe1C9s5Pm5lIzWwO0Q9jZx9t95o8CGR-eZGhN9_rbtYvY713d5SWcYmyqszBoEnL3hbClFX5gh84LEz21vgtWUgfmSO-iwNAhbVUQxFIaSAtu9N7c_nfqkLok3U1OUCt17UXTXdcVQKWRCwgUbv1nJl_GoxQd5dRjpr3Pe3yvThI-lykmVEpENUyPYp74KBkv9uejYHJNVEVYieinTYEcoEkj-cyZ-PHfYBmwBuIPUdNV4_pEdjgXMfEeMSckwST8Q6q51yVXgBBDCgdwgJJI4yqbSzmMfjxf84YI91Hy-Hh1oXS_34-Av_QI-SfV680Mpk19PyNyBZq-7OD-SOpIi0sQp4aTNCAu3nmY_vicu9q2svd7-h7uPIyj4CvXoM2KlsXaWSwe5c97HtnP1Qiu-HHKkhFLVI78VQCqKpoHeSbjkHFaeCWAkyCCPmN0kL2yl87zl76quNHTS9f2Rfan_QB2fC155y2iX2oSw6YNktBBCJFNlL6QmvCk0_LEFZpmAEF3vHxHzAryazxtr8aqvTlAH3peJXFTrXZAcZriJ57R5lS-j8UShIQ_uER0Q=w1920-h942-ft">

<p>These categorial fueatures (marital status, education and houseing) have not impact on supcription rate. Exception from this conclusion is the feature education, becouse the subcription rate of the iliterate shows higer rate of subscription.This is expected because this group does not have knowledge for better and sofisticated kinds of investment. <p>

<img src="https://lh3.googleusercontent.com/sD5lMSEh7AurJz7lMS1LlAw_RGF62QOZC8R4s4lSveCmCcNpba4fS8HcCO4lgbjk-BOZ4PwH74_JW_u1NKDaavWY6OzVlYHz1CO_vRfDDD4wdjQjdfqDXkcCs6D8s7b3HfDsnDNRTH8CsTrHitn_HNoug5QUFM205jbyicwcGNORROrQmLwmcbpw8ekRdygvyWJx_Ldm3DdF_Z6jDnO81ztyuo9zGLWYviM8gwdp4tEbt02_3IqwrUlbfKMbDf0-B83H_WSywzJhAV-PvUAvh-JD9ehmic_lu3pbfdczyr1VJcfcA7y67UvMsvKilNcUztX0dFolpAaNK-xF_3uCsMa7rpoQRuHEnhHHFA6XFmhMkXdcOvg3IaZ2Xds8D5V_WzKFUv_lzwlALNv7LXm49GC2Uu1_zhkkrIteQdam47zZ6fqOeZKjz1LLigL9lfhFi7iFWHzntrAfWlffGdrG1xcSV9Tg1odzFweMpi9xx0J5n269tvg57D4v-BnaVuY7TprbykKRWNVDryVm1dg1cPxT3lYsEyIXypiJt0vAKJCWISj2a0F8l4y-JmYKH9ATX-DZ5W8nQFSs9JGziMgA4uWnEsyL2ijpD94SEMnftiJX_xGuwe3ZjboxhGncBniY7pSt9Mceh618BzLypjuCxjQp5zL1r7wt0VDSft1S3nhlD2t3KJzSbP1QV_gDxRsnGtJ7Bw=w1920-h942-ft">

<p>The bank’s contact rate and clients’ response rate in each month have diffrent directions. This can be interpret on two ways. Either the bank starts to contact the clients when the demand of deposits starts to decrease or that the bank has bad timing for contacting. The contact rate is the highest in may and august and on other hand, the highest subscription rate occured in march, september and october</p> 

<p>For more :<q>Build a future where people live in harmony with nature.</q></p>

<p>From the above heatmap we can see that there are some numerical features which share a high correlation between them, e.g nr.employed and euribor3m these features share a correlation value of 0.95, and euribor3m and emp.var.rate share a correlation of 0.97, which is very high compared to the other features that we see in the heatmap.

<h3> Models implementation </h3>

<p>In order to be able to discuss the models and their accuracy first must be completed, the data processing, reprocessing, cleaning and data analysis. In this section we divide the test and training data and define the models that can solve this classification problem.
In our case, several models are defined and in the next picture we can see the progress and improvement of the accuracy of the models.</p>

<img src="https://lh3.googleusercontent.com/oqk0Ep8mT1hYEOwYxMcgsRyBFhuGRvZEWwqP64obqtThcOib3DU1y0QZL1yag5T1A2Ak_t1gQifWqgHx-rnOgzpDRS0AA48Tjm9CWaWOqrGEBJm-dZL1mhWMJjtuLS7aUeHnNlitPvzo-Bkkp2l4xAozyD0QHDhilt_XGglVaYpo-TZlBsdczGszb8rsZ8qJd8_Gsd3OddlGm4AitWqOTvMDoXa68JVLKJmF5PaYMJhM65wObJBcgoIaxZHJDN9q6pLMwttMni0oqp9ZftLlSAJz-gKdJuj3FOumfEJtlAQ50XTmORJ6E1-HCgLoNYlKdzNmkeGWXTyGvH0k7CRZDgbm8Rkq8utm0i3uc9fB1KsrdWDmLwrw_fj9dMiPG6eJ5jmXvLmzhJFZ6dKneehxlpDPCYZCUXnXgrWKvz3u0Frxnrqhd_CrwErdyvVULAH4YeXQFVQOepPtYt4SyBP5FIGu0npqbmx387waE5Go6HAdx8oYbU3XeQnsQL0uB54Ba4VosjI92vdlYce9paW-wYdLdUNuvNotvV_wAqlAYUCNXFirZzur1Bk6O3POwzwo9UJQ7lKr4k99va9rSJaxAM_n9acANKAtrwLMWayL8h9ngc7eM8j-UJi5rBKDxND7UQEOfg9JRapJM_lhBpE5kJzbC2xS1xKpDmsKisVae4uy2VadUDClhrexhBemA_p2hnikJw=w1920-h942-ft">
 
<p>From what has been shown, it is clear that Gradient Boosting and XGBoost give the best results. For example, XGBoost derived from chain of tree based models and has it roots in the very first Decision Tree Model. Each model had improvements over the previous one, making XGBoost and Gradient Boost most advanced and sophisticated models so far.</p>

<img src="https://lh3.googleusercontent.com/BMSG1uQmr5fD0JbLO98pSRxny6xBN7KMDZ3frLKBmdQcuEJ4ap3Ea5ITMG51DDu5Ylmsx12zJOPOFPnwXUYvbORwitF-u7oP1G87jpvQw9232KyZmZcAF0q_eKa3LFanEv7-trFzhpbv4J-9XcfeA1EaMFTm8qJuXkG3ZD8YdqsYtXYbdV1ARBO5i_ZYAgwqHoqoIch7-n_GJw9wad3gSYCM3Y7LFhQAbakIIEIrREsJZbYoygGrEzJd7rG050UlcXb81WwQVDBTN6jm9jhKcu_J5iy5RmUWs6ADLCXEgI6ASZaUu91UZsSumkvILXwtKnhLwmctCI-qNkmp5ubgA065NsBs6VjeAMBO0XiQ4aRUxUo6vAnic1_SAf3kQlkuwWC93RN5Rz4jVDwYCCl4m-qThihHdGaowsjXoeTgjdVpTVUfuq-VxyyjEPrG5-PI2Zb13HXH3a2PVUfCq4dWmaZcA44aOayxmkrrDjvNm2-0eGOqT6qhkCDNq206H5TFrbp5zIWE3N0rz40sPldqOar_132AB5IG31ZruM8rcc0gfMLNfM8yf-LKGj6VMV3qyA9PHxLsNbNY7DYsujrEr6DqnKDUwNIyvJJlNU0nIj-TYRZ1dIavuNBs1O88mtiuTSPJfhxPkDaN6UhxeaNDj2WSSPMqhegu5B8j27AR6OoedtKL0hFwlhlqXb5n60Q1BJ16YA=w1920-h942-ft">

<p>Both models have some predefined parameters and using them is not always best practice.
In our case the models with parameter adjustment give some slight improvement less than 0.2. Therefore, models with predefined parameters are used so that a trade-off can be made because the time spent on setup does not give us any significant improvements.</p>

</p>XGBoost gives the best results, but in the end it was able to identify slightly more than a half of positive outcomes, which tells that there must be other ways to improve it. Maybe we need more data or we need to modify what we have. The data science process never ends.</p>



<h3>Conclusion</h3>


<p>As George E. P. Box said: “all models are wrong, but some are useful”.</p>

  
</body>
</html>
