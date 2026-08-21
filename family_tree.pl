/*
   Family tree for Suwarna

   Facts are stored only once. Symmetric and derived relationships are handled
   by rules, which keeps the knowledge base small and easy to maintain.
*/

% Gender
male(krishna).
male(shankar).
male(shekhar).
male(sampurna).
male(suwarna).

female(sita).
female(shova).
female(devi).

% parent(Parent, Child)
parent(krishna, shankar).
parent(sita, shankar).
parent(krishna, shekhar).
parent(sita, shekhar).

parent(shankar, suwarna).
parent(shova, suwarna).

parent(shekhar, sampurna).
parent(devi, sampurna).

% Each marriage is recorded in only one direction.
married(krishna, sita).
married(shankar, shova).
married(shekhar, devi).

% Basic relationships
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

spouse(Person1, Person2) :- married(Person1, Person2).
spouse(Person1, Person2) :- married(Person2, Person1).

% setof/3 prevents duplicate sibling answers when two people share two parents.
sibling(Person1, Person2) :-
    dif(Person1, Person2),
    setof(CommonParent,
          (parent(CommonParent, Person1), parent(CommonParent, Person2)),
          [_ | _]).

brother(Brother, Person) :-
    male(Brother),
    sibling(Brother, Person).

sister(Sister, Person) :-
    female(Sister),
    sibling(Sister, Person).

% Grandparents
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

grandfather(Grandfather, Grandchild) :-
    male(Grandfather),
    grandparent(Grandfather, Grandchild).

grandmother(Grandmother, Grandchild) :-
    female(Grandmother),
    grandparent(Grandmother, Grandchild).

% Uncles and aunts include both blood relatives and relatives by marriage.
blood_uncle(Uncle, Person) :-
    male(Uncle),
    sibling(Uncle, Parent),
    parent(Parent, Person).

blood_aunt(Aunt, Person) :-
    female(Aunt),
    sibling(Aunt, Parent),
    parent(Parent, Person).

uncle(Uncle, Person) :- blood_uncle(Uncle, Person).
uncle(Uncle, Person) :-
    male(Uncle),
    spouse(Uncle, BloodAunt),
    blood_aunt(BloodAunt, Person).

aunt(Aunt, Person) :- blood_aunt(Aunt, Person).
aunt(Aunt, Person) :-
    female(Aunt),
    spouse(Aunt, BloodUncle),
    blood_uncle(BloodUncle, Person).

cousin(Person1, Person2) :-
    dif(Person1, Person2),
    parent(Parent1, Person1),
    parent(Parent2, Person2),
    sibling(Parent1, Parent2).

% Ancestor and descendant work for any number of generations.
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant).

descendant(Descendant, Ancestor) :-
    ancestor(Ancestor, Descendant).
