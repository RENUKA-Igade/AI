%Create a List
create_list(List) :-
    List = [1, 2, 3, 4, 5].

%Concatenate Lists
concatenate_lists(List1, List2, Result) :-
    append(List1, List2, Result).

%Delete Item from List
delete_item(Item, List, Result) :-
    select(Item, List, Result).




%Output
/*
 create_list(List).

 concatenate_lists([1,2,3], [4,5,6], Result).

 delete_item(3, [1,2,3,4], Result).
*/
