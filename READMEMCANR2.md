# BizOps Marketing Campaign Analysis Dashboard

This dashboard pack provides a detail analysis for your marketing campaigns. You can see the responses broken down <br>
by a specific campain, campaign responses by GEO and key KPI data like revenue and conversion for the campaigns. <br>

![Marketing Campaign Analysis](image/MCA.png)

# Prerequisites Highlights

1. Create a session property for your campaign (i.e. Web property pack - web\_utm\_campaign query string)
2. Create a session property for your campaign source (i.e. Web property pack - web\_utm\_source query string)
3. Create a session property for revenue (i.e. revenue - CSS selector)
4. Create a metric for the campaign session property (Metric: Useraction Duration split by Campaign/Geo)
5. Create a metric for the campaign source session property (Metric: Useraction Duration split by Source/Geo)
6. Create a metric for the campaign and source (Metric: Useraction Duration split by Campaign/Source)
7. Create a metric for the source and campaign (Metric: Useraction Duration split by Source/Campaign)
8. Create a metric for the revenue session property (Metric Revenue filtered on the last user journey step)
9. Mark the last user action step as a key user action for the user journey
