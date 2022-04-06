# altallinonestoreapi

This API is designed as an alternative to the allinonestoreapi: https://github.com/mahesh2247/allinonestoreapi/

It combines a simple UI which consists of a textarea to accept valid JSON input and process invoice all in the same page.

The API computational logic for the input is as follows :

 - 5% on medicines and Food
 - 5% on clothes below 1000 INR and 12% above 1000INR purchase
 - 3% on music cds/dvds
 - Flat 18% on the imported commodities.
 - Books are exempted from tax.
 - On every purchase I get a receipt that has the below information :
 - Date and Time of purchase
 - List of commodities, each with their final price, tax amount with the applicable rate
 - Total amount payable
 - Additionally, a 5% discount is applied by the store if the bill exceeds 2000INR.
 - The bill is sorted in the ascending order of the commodity names.

The API can be run directly from heroku cloud from the deployments menu in right hand corner of the github repo or here: https://altallinonestoreapi.herokuapp.com/

This API was created as a sample project for a sample use case as part of Interview Assessment.
