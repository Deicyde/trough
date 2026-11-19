---
declaration: theorem
origin: cited
lean: TauCeti.Approximation.Converges.computableIn_jump
statement: formalized
proof: formalized
---

# Limit Lemma, computing the limit

If the stages `f s` are computable in `Z`, uniformly in
`s`, and converge pointwise to `g`, then `g` is computable in the jump `Z'`.

```lean
TauCeti.Approximation.Converges.computableIn_jump {Z : Set ℕ} {f : ℕ → ℕ → ℕ} {g : ℕ → ℕ}
  (h : TauCeti.Approximation.Converges f g) (hf : ComputableIn₂ {Z.oracle} f) :
  ComputableIn {Z.jump.oracle} g
```

## Depends on

- [Set.jump](set-jump.md)

## Proof depends on

- [Adequacy](adequacy.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Approximation.Converges.computableIn_jump`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/Limit.html#TauCeti.Approximation.Converges.computableIn_jump).

## Sources

- [Tau Ceti documentation: `TauCeti.Approximation.Converges.computableIn_jump`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/Limit.html#TauCeti.Approximation.Converges.computableIn_jump)
- [Source of `TauCeti.Approximation.Converges.computableIn_jump` in TauCeti/Computability/Approximation/Limit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/Approximation/Limit.lean#L68)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
