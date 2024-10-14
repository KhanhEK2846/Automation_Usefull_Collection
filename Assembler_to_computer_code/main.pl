#!/usr/bin/perl
use strict;
use warnings;
my @REGArr = ("","00000",'$zero',"00000",'$at',"00001",'$v0',"00010",'$v1',"00011",'$a0',"00100",'$a1',"00101",'$a2',"00110",'$a3',"00111",'$t0',"01000",'$t1',"01001",'$t2',"01010",'$t3',"01011",'$t4',"01100",'$t5',"01101",'$t6',"01110",'$t7',"01111",'$s0',"10000",'$s1',"10001",'$s2',"10010",'$s3',"10011",'$s4',"10100",'$s5',"10101",'$s6',"10110",'$s7',"10111",'$t8',"11000",'$t9',"11001",'$k0',"11010",'$k1',"11011",'$gp',"11100",'$sp',"11101",'$fp',"11110",'$ra',"11111");
my @OPCODEArr =("add","000000","addi","001000","addiu","001001","addu","000000","and","000000","andi","001100","beq","000100","bne","000101","j","000010","jal","000011","jr","000000","lbu","100100","lhu","100101","ll","110000","lui","001111","lw","100011","nor","000000","or","000000","ori","001101","slt","000000","slti","001010","sltiu","001011","sltu","000000","sll","000000","srl","000000","sb","101000","sc","111000","sh","101001","sw","101011","sub","000000","subu","000000");
my @FUNCTArr =("add","100000","addu","100001","and","100100","jr","001000","nor","100111","or","100101","slt","101010","sltu","101011","sll","000000","srl","000010","sub","100010","subu","100011");
my @LabelArr=();

my %REG = @REGArr;
(my $IDr,my $namer)= each %REG;
my %OPCODE=@OPCODEArr;
(my $IDo,my $nameo)= each %OPCODE;
my %FUNCT = @FUNCTArr;
(my $IDf,my $namef)= each %FUNCT; 

open my $f,">abc.txt";
print $f '.data',"\n","apple:   .assciiz 1,2,3,4","\n",'.text',"\n",'add $t0,$t1,$t2',"\n",'%nothing',"\n",'noone:  addi $s0,$s1,10',"\n",'jr $ra',"\n","j annyone","\n","annyone:","\n",'sll $t2,$s0,4',' %nothing',"\n",'lw $t0,12($s0)',"\n";
close $f;

sub del_comment
{
    open my $f,'<',@_;
    open my $t,">cba.txt";
    my @c;
    while(<$f>)
    {
        @c=split /%.*/,$_;
        if($c[0] ne '')
        {
            print $t @c;
        }
    }
    close $f;
    close $t;
}




sub cre_label
{
    open my $f,'<',@_;
    open my $t,">Text.txt";
    open my $d,">Data.txt";
    my $PC=0;
    while(<$f>)
    {
        if(/.data/)
        {
            $PC +=4;
            next;
        }
        if(/.text/) 
        {
            $PC +=4;
            last;
        }
        if(/:/)
        {
            print $d $_;
            my @tmp = split /:/,$_;
            push(@LabelArr,$tmp[0]);
            push(@LabelArr,$PC);
        }
        
        $PC +=4;
    }
    close $d;
    while(<$f>)
    {
        if(/:/)
        {
            my @tmp = split /:/,$_;
            push(@LabelArr,$tmp[0]);
            push(@LabelArr,$PC);
            if($tmp[1])
            {
                $tmp[1]=~ s/^\s+//;
                print $t $tmp[1];
            }
        }
        else
        {
            if($_ ne '')
            {
                print $t $_;
            }
        }
        $PC+=4;
    }
    close $f;
    close $t;
    unlink (@_);
}

sub Binary
{
    my @a = @_;
    my @data;
    while($a[0]>=1)
    {
        my $b = $a[0] %2;
        unshift(@data,$b);
        $a[0]= ($a[0]- $b)/2;
    }
    return @data;
}

sub printfile
{
    open my $f,'<',@_;
    print<$f>;
    print "\n";
    close $f;
}

del_comment 'abc.txt';
printfile "cba.txt";
cre_label 'cba.txt';
my %Label = @LabelArr;
(my $IDl, my $namel) = each %Label;

sub AssToComp
{
    open my $f,'<',@_;
    open my $t,">final.txt";
    while(<$f>)
    {
        my @c= split / /,$_;
        print $t $OPCODE{$c[0]};
        chomp($c[1]);
        my @p= split /,/, $c[1];
        if($OPCODE{$c[0]} == 100011 || $OPCODE{$c[0]} == 101011 || $OPCODE{$c[0]} == 100101 || $OPCODE{$c[0]} == 100100 || $OPCODE{$c[0]} == 110000 || $OPCODE{$c[0]} == 101000 ||$OPCODE{$c[0]} == 101001 )
        {
            my @tmp = split /\(/ , $p[1];
            chop($tmp[1]);
            $p[1] = $tmp[1];
            push(@p, $tmp[0]);
        }
        if(!$p[1] and !$p[2])
        {
            $p[1]=$p[0];
            $p[0]=$p[2]="";
        }
        if($OPCODE{$c[0]} == 0 )
        {
            
            if($FUNCT{$c[0]}==0 || $FUNCT{$c[0]}==10 )
            {
                my @i = Binary $p[2];
                print $t $REG{""},$REG{$p[1]},$REG{$p[0]};
                for(my $j=1;( $j + scalar(@i))<=5;++$j )
                {
                    print $t 0;
                }
                print $t @i;
                print $t $FUNCT{$c[0]};
                
            }
            else
            {
                print $t $REG{$p[1]},$REG{$p[2]},$REG{$p[0]},$REG{""},$FUNCT{$c[0]};
            }
        }
        else
        {
            if($OPCODE{$c[0]}==10 || $OPCODE{$c[0]}== 11)
            {
                my @i= Binary $Label{$p[1]};
                 for(my $j=0;( $j + scalar(@i))<26;++$j )
                {
                    print $t 0;
                }
                print $t @i;
            }
            else
            {
                my @i;
                if($OPCODE{$c[0]}==100||$OPCODE{$c[0]}==101)
                {
                    @i = Binary $Label{$p[2]};
                }
                else
                {
                    @i = Binary $p[2];
                }
                print $t $REG{$p[1]},$REG{$p[0]};
                for(my $j=0;( $j + scalar(@i))<16;++$j )
                {
                    print $t 0;
                }
                print $t @i;
                
            }
        }
        
        print $t "\n";
    }
    close $f;
    close $t;
}

AssToComp 'Text.txt';
printfile 'final.txt';












