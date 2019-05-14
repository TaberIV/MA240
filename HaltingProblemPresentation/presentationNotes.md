# Halting Problem

## History

- Turing, the father of computers
- Turing introduced the Turing Machine to prove this in 1936

## Turing Machine

- Turing machine is made of a few parts
  - Q is a finite, non-empty set of _states_
  - Gamma is a finite, non-empty set of _tape alphabet symbols_
  - b is an element of Gamma known as the _blank symbol_
  - q0 is the initial state
  - F is a subset of Q where elements of F are accept states
  - delta is the transiton function

## Turing Machine Example

```turing machine
init: q0
accept: qAccept

q0,0
q0,0,>

q0,1
q1,1,>

q1,0
q2,0,>

q1,1
q0,1,>

q2,0
q1,0,>

q2,1
q2,1,>

q0,_
qAccept,_,-
```

## Halting Problem Proof

Assume there exists some function H(i, x) where H returns 1 if i terminates on x
and 0 otherwise. If we define some function g(x)

```psudo
if H(g, x)
  loop forever
```

A more formal way to define this is as follows. h(i, x) = {1, if halt else 0}
g(i) = {0 if f(i,i) = 0 else undefined}
f is a totally computable binary function.

1. f(e, e) = 0, g(e) = 0, h(e, e) = 1.
2. f(e, e) != 0, g(e) is undefined, h(e, e) = 0

consider f = h, for the case e = g

We have a contradiction in case 1 because f(e, e) != h(e, e).
We have a contradiction in case 2 because if g(g) is undefined then h(e, e) = 0
However f(e, e) must be 1 for g(e) to be undefined

## Modern Research

Complilers are regular languages, they always halt.

Interpreters are turing complete, they introduce non-halting.

- Coq is a formal proof management system. It provides a formal language to write mathematical definitions, executable algorithms and theorems together with an environment for semi-interactive development of machine-checked proofs
