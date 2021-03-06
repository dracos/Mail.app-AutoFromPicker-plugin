Mail.app-AutoFromPicker-plugin
==============================

Automatically keep work and personal OS X Mail.app accounts separate.

Here, it does two things:

1. When you hit reply to a mail, it scans the recipients and sets the From
   account accordingly.

2. When you hit send, it does a final check of the recipients and brings up a
   dialogue box (though given 1 it probably won't have to do that, as it'll
   already be set correctly).

Install
-------

If you haven't installed Mail bundles before, you might need to run the two
defaults write commands as given on http://www.cs.unc.edu/~welch/MailFollowup/
under the manual install instructions.

0. Quit Mail.
1. Clone this repository
2. Copy config.py.EXAMPLE to config.py and edit to have your account details
   and domains/emails you're interested in. Make sure the account matches what
   appears in Mail's From drop down exactly. Also pick which features you want
   to be on (True) or off (False).
3. If on 10.9, generate yourself a self-signed certificate.
4. Run make.sh "Your Certificate Name" in this directory. This will build the
   app and move it into Mail's Bundles directory.
5. Start Mail.

Da-da! If it doesn't work, run Console and see what error it's outputting when
it goes wrong, and let me know.


Based on Attachment Scanner Plugin by James Eagan http://eaganj.free.fr/code/mail-plugin/

and the code was written by Matthew Somerville.

