---
declaration: theorem
origin: cited
lean: TauCeti.exists_simple_not_turingReducible, TauCeti.exists_simple_not_turingReducible_code
statement: formalized
proof: formalized
---

# Sacks's theorem [S, VII.3.1]

for every noncomputable c.e. set `C`, there is a simple set
`A` with `C ≰_T A`.

```lean
TauCeti.exists_simple_not_turingReducible {C : Set ℕ} (hC : REPred fun x => x ∈ C)
  (hnc : ¬ComputablePred fun x => x ∈ C) : ∃ A, A.Simple ∧ ¬TuringReducible C.oracle A.oracle
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Adequacy](../computability-theory-and-finite-injury-construct/adequacy.md)
- [Soare's Lemma 1](soares-lemma-1.md)
- [TauCeti.Oracle.Single.Code](../computability-theory-and-finite-injury-construct/tauceti-oracle-single-code.md)
- [TauCeti.Priority.injurySet](../computability-theory-and-finite-injury-construct/tauceti-priority-injuryset.md)
- [The use principle](../computability-theory-and-finite-injury-construct/the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_simple_not_turingReducible`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/ConeAvoiding.html#TauCeti.exists_simple_not_turingReducible).

## Other forms

**Sacks's theorem [S, VII.3.1], with an index.** Formalized in Tau Ceti as [`TauCeti.exists_simple_not_turingReducible_code`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/ConeAvoiding.html#TauCeti.exists_simple_not_turingReducible_code).

```lean
TauCeti.exists_simple_not_turingReducible_code {C : Set ℕ} (hC : REPred fun x => x ∈ C)
  (hnc : ¬ComputablePred fun x => x ∈ C) :
  ∃ d, {x | (d.eval x).Dom}.Simple ∧ ¬TuringReducible C.oracle {x | (d.eval x).Dom}.oracle
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_simple_not_turingReducible`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/ConeAvoiding.html#TauCeti.exists_simple_not_turingReducible)
- [Source of `TauCeti.exists_simple_not_turingReducible` in TauCeti/Computability/Simple/ConeAvoiding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Simple/ConeAvoiding.lean#L207)
