# Bulk User Account Manipulation in Active Directory:blue_heart:

@Author: Aaron Law

@Last Update: 2019-06-06

@Env: Python 3.6+, Powershell 5.1

Purpose:

Can we mass manipulation user accounts in Active Directory via scripting? We are going to create, edit, and remove user accounts in AD via Powershell.

An example of data requirement of cmdlet could be:

```
fn,firstname,lastname,
```

The above data requirement defines the output of Python script we are going to made.



## 1. Prepare bulk user information in Python

Prepare a `.csv` file storing user information that we go to import into AD.

A sample format is:

```
User-name,First-name,Last-name
```

(The first line is the column name of CSV and they are going to be variable names in the next part. The column name must be exact match the variable names in Powershell. Be cation of whitespace.)





## 2. Issue commands for user account manipulation

Issue the following cmdlet in Powershell, or save it as a `.ps1` and execute.

```powershell
get-help Set-ADUser
```





Reference:

