#!/usr/bin/env python2
#-*-coding:utf-8-*-
# modificare per eliminare accenti

def abcd():
    print "\n-------------------"
    print "THE ALPHABETIZER 2014"
    print "by orC°"
    print "This is a very small program that sorts"
    print "the letter of your name in an alphabetical order."
    print "It is supposed to be a perfectly useless software"
    print "or a 'f-utility'. "
    print "It comes after Alighiero Boetti ideas"
    print "and it is distribuited under Creative Commons License."
    print "--------------------\n"

    print "Write here your name"
    name = raw_input('>')
    tupleList = [str(x.lower()) for x in name]
    tupleList.sort()

    #list[:] = [x[1] for x in tupleListn
    print "Your alphabetized name is:"
    #return [x[1] for x in tupleList]

    print ''.join(tupleList).replace(" ", "").capitalize()
abcd()
