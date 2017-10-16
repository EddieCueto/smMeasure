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

#GASMAN("collect");
#RANDOM_SEED(1);

testy_testy := 4;

#G := SymmetricGroup(testy_testy);
#G := CyclicGroup(testy_testy);
G := DihedralGroup(testy_testy);

#this line is a test for git in fedora 25 for github :P

sz := Size(G);
H := AsList(G);

l := [];

for h in [1 .. sz] do
  Add(l,[]);
od;

for i in [1 .. sz] do
  for j in [1 .. sz] do
    Add(l[i],Float(M_i(H[i],H[j])));
    #if i = j then
      #break;
    #fi;
  od;
od;

#time := Float(Runtime());
#PrintTo("time.txt",time);

PrintTo("SymMat.txt",l);
PrintTo("GrpSz.txt",sz);
