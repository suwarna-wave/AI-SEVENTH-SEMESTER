/*
   Family Tree Expert System in Prolog

   Facts describe people, marriages, and parent relationships.
   Rules infer other relationships from those facts.
*/

% -----------------------------------------------------------------------------
% Gender facts
% -----------------------------------------------------------------------------

male(ram).
male(hari).
male(shyam).
male(anil).
male(suresh).

female(sita).
female(gita).
female(maya).
female(rita).
female(nita).

% -----------------------------------------------------------------------------
% Marriage facts
% Store each marriage once; spouse/2 makes the relation work both ways.
% -----------------------------------------------------------------------------

married(ram, sita).
married(hari, maya).
married(shyam, gita).

% -----------------------------------------------------------------------------
% Parent facts: parent(Parent, Child)
% -----------------------------------------------------------------------------

parent(ram, hari).
parent(sita, hari).
parent(ram, gita).
parent(sita, gita).

parent(hari, anil).
parent(maya, anil).
parent(hari, rita).
parent(maya, rita).

parent(shyam, suresh).
parent(gita, suresh).
parent(shyam, nita).
parent(gita, nita).

% -----------------------------------------------------------------------------
% Derived relationship rules
% -----------------------------------------------------------------------------

father(Father, Child) :-
    male(Father),
    parent(Father, Child).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

child(Child, Parent) :-
    parent(Parent, Child).

son(Son, Parent) :-
    male(Son),
    parent(Parent, Son).

daughter(Daughter, Parent) :-
    female(Daughter),
    parent(Parent, Daughter).

spouse(Person1, Person2) :-
    married(Person1, Person2).
spouse(Person1, Person2) :-
    married(Person2, Person1).

sibling(Person1, Person2) :-
    dif(Person1, Person2),
    parent(CommonParent, Person1),
    parent(CommonParent, Person2).

brother(Brother, Person) :-
    male(Brother),
    sibling(Brother, Person).

sister(Sister, Person) :-
    female(Sister),
    sibling(Sister, Person).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

grandfather(Grandfather, Grandchild) :-
    male(Grandfather),
    grandparent(Grandfather, Grandchild).

grandmother(Grandmother, Grandchild) :-
    female(Grandmother),
    grandparent(Grandmother, Grandchild).

uncle(Uncle, Person) :-
    male(Uncle),
    sibling(Uncle, Parent),
    parent(Parent, Person).

aunt(Aunt, Person) :-
    female(Aunt),
    sibling(Aunt, Parent),
    parent(Parent, Person).

cousin(Person1, Person2) :-
    dif(Person1, Person2),
    parent(Parent1, Person1),
    parent(Parent2, Person2),
    sibling(Parent1, Parent2).

% Base case: a parent is an ancestor.
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).

% Recursive case: an ancestor of a parent is an ancestor of the child.
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant).

