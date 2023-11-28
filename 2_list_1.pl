%Create a List
create_list(List) :-
    List = [1, 2, 3, 4, 5].

%Check Membership
is_member(Element, List) :-
    member(Element, List).

%Calculate Length
list_length(List, Length) :-
    length(List, Length).


%Output
/*
 create_list(List).

 is_member(3,[1,2,3,4,5]).

 list_length([1,2,4,5],Length).
*/
