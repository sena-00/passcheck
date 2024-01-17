# Passcheck - Password Strength Checker

Pretend you want to change your password. You are not sure if your password is complex enough, or perhaps you want to check the strength for a password you are currently using.
Passcheck *solves this problem!*

# Usage and funnctions
The application has been created in python. I left a .exe file in the `dist\passcheck` folder. You can also use the python file in the main folder.
>[!WARNING]
>When running the application on Windows you may receive a virus alert message.

After opening the app, you will be greeted with a GUI. You may now insert the desired password in the blank space.
When testing the password there are only *two* possible outcomes:

```diff
- Weak Password - Complexity criteria not met
+ Strong Password - Complexity criteria met
```

But what are these criterias?

+ Checks if the password is over 6 chars.
+ Checks if the password has uppercase.
+ Checks if the passwword has lowercase.
+ Checks if the password has numbers.

https://github.com/sena-00/passcheck/assets/156020094/1636ebaf-6556-4cfd-abdf-9eaf65574aae

The logic for this app is centralized in `for` and `if` loops.
This can be found in found in the line 79. The rest of the code is mostly visual changes and buttons/actions customization.

>[!NOTE]
>This application has been developed for educational purposes only. There are (many) mistakes on it.
>Prior to this, i had not python experience.

