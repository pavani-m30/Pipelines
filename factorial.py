Here is your **complete, expanded, enterprise‑grade AI prompt** that includes:

*   Every feature you described
*   Full insurance flows (Vehicle, Health, Life, Travel, Home)
*   Database schema
*   Customer + Operations team
*   Notifications system
*   Backend + Frontend expectations
*   Real‑world insurance logic
*   Clean structure for an AI to build the entire application

You can paste this into ANY AI app (Copilot Workspace, ChatGPT, Replit Agent, Cursor, Codeium, etc.) and it will know exactly what to build.

***

FULL‑STACK INSURANCE APPLICATION – COMPLETE AI PROJECT PROMPT (ALL FEATURES INCLUDED)

Build a full‑stack **Insurance Management Application** with web + mobile responsive UI, backend APIs, authentication, customer workflows, operations workflows, payments, notifications, and database.

This project must include the following:

\==================================================

1.  LOGIN & AUTHENTICATION MODULE
    \==================================================
    Create a login page with fields:

*   Username
*   Password
*   User type: Customer or Operations Team

Behaviors:

*   Customer login → Customer Home
*   Operations login → Operations Dashboard
*   Forgot Password (via OTP/email link)
*   Multi‑factor authentication (optional toggle)
*   Captcha validation

\==================================================
2\. CUSTOMER PORTAL
===================

\======================
2.1 Home Page
=============

Top bar:

*   Notification Bell
*   Profile Icon with dropdown

Dropdown pages:

*   Change Mobile Login
*   KYC Verification Page
*   Settings
*   My Activity
*   Logout

Home widgets:

*   Insurance categories
*   Recommended plans
*   Offers & discounts banner
*   Quick shortcuts (Renew, Claims, Pay Due Premium)

Notifications include:

*   KYC approval/rejection
*   Policy purchase status
*   Claim updates
*   Payment successful
*   Payment due
*   Renewal reminders
*   Fraud alert

\======================
2.2 Explore Insurance
=====================

Insurance Categories:

*   Vehicle Insurance
*   Health Insurance
*   Life Insurance
*   Travel Insurance
*   Home Insurance
*   Corporate Insurance (optional)

Each category opens:

*   Overview
*   Benefits
*   Coverage details
*   FAQs
*   Buy Insurance flow

\==================================================
3\. INSURANCE BUY FLOWS (ALL CATEGORIES)
========================================

***

3.1 VEHICLE INSURANCE FLOW  
(template for other categories)
-------------------------------

Ask step-by-step:

1.  Vehicle Type (2W/4W)
2.  RTO
3.  City
4.  Brand
5.  Model
6.  Variant
7.  Registration year
8.  Previous insurer
9.  Claim history
10. Fetch IDV + NCB autocalc

Quotes Page:

*   Show multiple insurer quotes
*   Show premium, IDV, add-ons, ratings
*   Buttons:
    *   Buy Policy
    *   Compare Plans

Compare Page:

*   Side-by-side insurer comparison

Buy Policy Flow:

*   Policy Summary
*   Premium split
*   Add-on selection
*   Customer details autofill
*   Payment page:
    *   UPI, Card, Netbanking
    *   Dummy payment
    *   Dummy receipt download

Rules:

*   Customer cannot buy the same policy until current policy ends

***

## 3.2 HEALTH INSURANCE FLOW

Ask:

*   Age
*   Gender
*   City
*   Hospital coverage requirement
*   Sum insured
*   Pre-existing diseases
*   Family members (floater option)

Show:

*   Quotes
*   Coverage comparison
*   Add-ons (room rent waiver, maternity, AYUSH, etc.)
*   Buy + Payment flow same as vehicle

***

## 3.3 LIFE INSURANCE FLOW

Ask:

*   Age
*   Occupation
*   Income
*   Tobacco consumption
*   Sum assured
*   Policy term
*   Medical history

Show quotes:

*   Premium
*   Maturity benefit
*   Riders
*   Claim settlement ratio

Purchase flow same

***

## 3.4 TRAVEL INSURANCE FLOW

Ask:

*   Destination
*   Travel dates
*   Number of travelers
*   Age of each traveler
*   Purpose (tour/business)

Show:

*   Medical cover
*   Travel delays
*   Loss of baggage
*   Emergency evacuation

Then buy + payment

***

## 3.5 HOME INSURANCE FLOW

Ask:

*   Property type (flat/house)
*   Ownership status
*   Built year
*   Carpet area
*   Address
*   Security devices installed

Show available plans + buy

\==================================================
4\. PAYMENT MODULE
==================

Payments Page:

*   Next due date
*   Remaining months
*   Premium amount
*   Payment history
*   Auto‑pay toggle
*   Dummy payment integration
*   Dummy receipt PDF

\==================================================
5\. BOTTOM NAVIGATION BAR (CUSTOMER)
====================================

Tabs:

*   Home
*   Policies
*   Claims
*   Support

Policies Page:

*   My Policies
*   Available Policies
*   Renewal Policies
*   Downloads (policy documents)

\==================================================
6\. CLAIMS MODULE (CUSTOMER)
============================

Features:

*   Submit claim
*   Upload documents/photos/videos
*   Track claim status
*   Claim timeline with timestamps
*   Chat with support (dummy chat)

Statuses:

*   Submitted
*   Under review
*   More documents required
*   Approved
*   Rejected
*   Paid

\==================================================
7\. OPERATIONS TEAM PORTAL
==========================

***

## 7.1 Dashboard

Show:

*   Total customers
*   KYC pending
*   Claims pending
*   Fraud alerts
*   Revenue summary
*   Active policies
*   Renewals due

***

## 7.2 KYC Module

*   View KYC submissions
*   Approve / Reject
*   Ask for re-upload
*   Mark as suspected fraud
*   Auto-verification scoring (dummy)

***

## 7.3 Claims Management

*   View submitted claims
*   Validate documents
*   Approve / Reject
*   Set approved amount
*   Flag fraud
*   Assign claim investigator (dummy)
*   Close claim

***

## 7.4 Notification Broadcasting

Operations can send:

*   Payment due
*   Payment successful
*   Claim updates
*   KYC status
*   Renewal reminders

***

## 7.5 Underwriting Panel

*   Risk scoring
*   Premium adjustments
*   Customer risk profiles
*   Fraud indicators

\==================================================
8\. REAL-TIME NOTIFICATION SYSTEM
=================================

Methods:

*   In-app notifications
*   Email alerts
*   SMS alerts (dummy)
*   Bell icon notifications

\==================================================
9\. SUPPORT MODULE
==================

*   Raise ticket
*   Chat with support
*   Track ticket status
*   Ticket escalations

\==================================================
10\. GENERAL SYSTEM FEATURES
============================

*   Responsive web + mobile UI
*   Dark mode
*   Multi-language support
*   Image/document upload
*   Secure sessions
*   Auto logout
*   Logging and monitoring
*   Error pages

\==================================================
11\. DATABASE SCHEMA (INCLUDE ALL TABLES)
=========================================

Include these tables with full relationships:

users  
customer\_profiles  
operations\_team  
kyc\_submissions  
insurance\_categories  
policy\_master  
vehicle\_details  
quotes  
purchased\_policies  
payments  
claims  
claim\_timeline  
notifications  
renewal\_reminders  
support\_tickets  
audit\_logs  
offers\_and\_discounts  
document\_vault

\==================================================
12\. BACKEND REQUIREMENTS
=========================

Build APIs for:

*   Auth
*   Customers
*   KYC
*   Policies
*   Vehicle data
*   Quotes
*   Purchases
*   Payments
*   Claims
*   Notifications
*   Operations team actions
*   Support tickets
*   Dashboard analytics

\==================================================
13\. TECHNOLOGY STACK (SUGGESTED)
=================================

Frontend:

*   React / Next.js / Flutter Web / Angular

Backend:

*   Node.js (Express/NestJS)
*   or Django REST
*   or Spring Boot

Database:

*   PostgreSQL or MySQL
*   Redis for caching

Authentication:

*   JWT + Refresh tokens

Storage:

*   AWS S3 / Firebase Storage for documents

***


