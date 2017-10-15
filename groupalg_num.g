#############################################################
#                                                           #
#  This GAP file will be used to test the M_i distance in   #
#  some groups with big order.                              #
#  Algorithm by Eduardo Cueto-Mendoza                       #
#                                                           #
#############################################################

M_i := function(g,h)  # this is the similarity measure
  local i, chk, tmp1, tmp2;
  i := 0;
  chk := 0;
  while chk = 0 do
    if g = h then
       return 1/(i+1);
      chk := 1;
    fi;
    if g <> h then
      i := i + 1;
      tmp1 := g * h;
      tmp2 := h * g;
      g := tmp1;
      h := tmp2;
    fi;
    if i > 10 then
      return 0;
    fi;
  od;
end;

testy_testy := 10;
time_test := [];
#add_t := 1;

for rr in [1..testy_testy] do
  Add(time_test,[]);
od;

for r in [1..testy_testy]  do  # final time test

GASMAN("collect");
RANDOM_SEED(1);

G := SymmetricGroup(r);
#G := CyclicGroup(r);
#G := DihedralGroup(r);
sz := Size(G);
H := AsList(G);

l := [];

for h in [1 .. sz] do
  Add(l,[]);
od;

for i in [1 .. sz] do
  for j in [1 .. sz] do
    Add(l[i],Float(M_i(H[i],H[j])));
  od;
od;

time := Float(Runtime());

Add(time_test[r],time);

#add_t := add_t + 1;

od;  # final time test

PrintTo("time.txt",time_test);
