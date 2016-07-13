#!/usr/bin/perl  -W
use Getopt::Long;
use Data::Dumper;
use Net::SMTP;
use Switch;
use POSIX  qw(strftime);



 my $curtime = strftime "%Y%m%d%H%M", localtime;
 my $sub =  "Msg";
 my $body = "CMS : $curtime";

sub send_mail
{
   my ($mailhost, $from, $to, $sub, $body, $user, $pass,  $debug);

   $mailhost  = shift;
   $from      = shift;
   $to        = shift;
   $sub       = shift;
   $body      = shift;
   $user      = shift;
   $pass      = shift;
   $debug     = shift;

 my $msub = "$sub: $curtime\n\n";
 my $msg = "MIME-Version: 1.0\n"
     . "From: $from\n"
     . "To: $to\n"
     . "Subject: $msub\n\n"
     . "$body\n";


#
#  Open a SMTP session
#

$smtp = Net::SMTP->new($mailhost,
                       Hello => $domain,
                       Debug => $debug,
                       Timeout => 30);


if(!defined($smtp) || !($smtp))
{


       #&writelog($logfile, "$curtime # SMTP ERROR: Unable to open smtp session\n");

        print "SMTP ERROR: Unable to open smtp session.\n";
        exit 1;

  #      print "SMTP ERROR: Unable to open smtp session.\n";
  #      return 0;
}

#  Pass Authen , exit if error



       if ( defined ( $user && $pass ))
        {

             #$smtp->auth( 'PLAIN', $user, $pass);
             if ( ! ($smtp->auth($user, $pass)) )
            {
                 print "Authen error";
                 return 0;
            }
        }

# Pass the 'from' email address, exit if error
        if (! ($smtp->mail( $from ) ) )
        {
            return 0;
        }

# Pass The recipient address(es)

if (! ($smtp->recipient( ( ref($to) ? @$to : $to ) ) ) )
       {
            return 0;
       }
# Send the message

$smtp->data();
$smtp->datasend($msg);
$smtp->dataend();


$smtp->quit;
      return 1;
}

sub synctex {
  print "Usage: zmail.pl\n";
  print "\t-s {subject}\n";
  print "\t-b {body}\n";
  print "\t-t {to} \n";
  print "\t-f {from}\n";
  print "\t-h {host}\n";
  print "\t-u {user}\n";
  print "\t-p {pass}\n";

}


  GetOptions ("subject=s" => \$sub,    # string
              "to=s"    => \$to,      # string
              "from=s"  => \$from,   # flag
              "host=s"  => \$host,
              "body=s"  => \$body,
              "user=s"  => \$user,
              "pass=s"  => \$pass,

)
  or die("Error in command line arguments\n");




#if(! defined ($sub && $to && $from && $host && $body)){
if(! defined ($to && $from && $host )){
    synctex();
}else {

   if ( defined ($user &&  $pass)) {

          send_mail ($host, $from, $to, $sub, $body, $user, $pass, 1);
      }else {
          $user='';
          $pass='';
          send_mail ($host, $from, $to, $sub, $body, $user, $pass, 1);
        }
}
