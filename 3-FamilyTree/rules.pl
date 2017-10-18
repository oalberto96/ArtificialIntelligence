grandparent(X,Y):-parent(X,A),parent(A,Y).
brother(X,Y):-X\=Y, parent(A,X),parent(B,X),A\=B,parent(A,Y),parent(B,Y),write(A),write(B).
half-brother(X,Y):-X\=Y,parent(A,X),parent(B,X),A\=B,parent(A,Y),parent(D,Y),A\=D,B\=D.
uncle(X,Y):-brother(X,A),parent(A,Y).
brother-in-law(X,Y):-husbands(X,A),brother(A,Y).
cousin(X,Y):-parent(A,Y),parent(B,X),A\=B,brother(A,B).
daugther-in-law(X,Y):-female(Y),husbands(A,Y),parent(X,A).
son-in-law(X,Y):-male(Y),husbands(A,Y),parent(X,A).
