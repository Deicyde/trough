---
declaration: theorem
origin: cited
lean: Jacobson.jacobson_conjecture, Jacobson.jacobson_conjecture_of_comm_ring, Jacobson.jacobson_conjecture_of_right_noetherian
statement: formalized
---

# Jacobson Conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Jacobson's_conjecture)
> - [He1965]: Herstein, I. N. (1965), "A counterexample in Noetherian rings",
>   Proceedings of the National Academy of Sciences of the United States of America, 54 (4): 1036–1037
>   https://pmc.ncbi.nlm.nih.gov/articles/PMC219788/
> - [Ja1956]: Jacobson, Nathan. Structure of rings. Vol. 37. American Mathematical Soc., 1956.
> - [Le1977]: Lenagan, T. H. (1977), "Noetherian rings with Krull dimension one",
>   J. London Math. Soc. Series 2, 15 (1): 41–47
>   https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s2-15.1.41

*Quoted from [FormalConjectures/Wikipedia/Jacobson.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Jacobson.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result.

## `Jacobson.jacobson_conjecture`

Open: stated without proof.

> The Jacobson conjecture (in its modern form):
> In a (noncommutative) ring which is left and right Noetherian,
> the intersection of the powers of the Jacobson ideal is trivial

```lean
theorem jacobson_conjecture :
    ∀ (R : Type) [Ring R] [IsNoetherianRing R] [IsRightNoetherianRing R],
      JacobsonConjectureFor R
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Jacobson.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Jacobson.lean#L51).

## `Jacobson.jacobson_conjecture_of_comm_ring`

Textbook result, stated without proof.

> For commutative rings this is the case as a consequence of Krull's intersection theorem.

```lean
theorem jacobson_conjecture_of_comm_ring (R : Type u) [CommRing R] [IsNoetherianRing R] :
    JacobsonConjectureFor R
```

Category `textbook`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Jacobson.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Jacobson.lean#L58).

## `Jacobson.jacobson_conjecture_of_right_noetherian`

Solved: stated here without proof.

> Originally, on page 200 of [Ja1956], Jacobson asked if the Jacobson conjecture holds for all right
> Noetherian rings. However in [He1965] Herstein constructs a right Noetherian ring for which the
> Jacobson conjecture does not hold.

```lean
theorem jacobson_conjecture_of_right_noetherian :
    ¬ ∀ (R : Type) [Ring R] [IsRightNoetherianRing R], JacobsonConjectureFor R
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Jacobson.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Jacobson.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Jacobson.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Jacobson.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Jacobson's_conjecture)
