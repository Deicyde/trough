---
declaration: theorem
origin: cited
lean: TauCeti.rademacherMoment_le_kahaneConst_mul
statement: formalized
proof: formalized
---

# Kahane's inequality

in any real normed space and for all `0 < p` and `0 < q`,
`rademacherMoment q x ≤ kahaneConst p q * rademacherMoment p x`.

```lean
TauCeti.rademacherMoment_le_kahaneConst_mul.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι]
  [DecidableEq ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] {p q : ℝ} (hp : 0 < p) (hq : 0 < q)
  (x : ι → E) :
  TauCeti.rademacherMoment q x ≤ ↑(TauCeti.kahaneConst p q) * TauCeti.rademacherMoment p x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iterated doubly-exponential Rademacher tail bound](iterated-doubly-exponential-rademacher-tail-boun.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.rademacherMoment_le_kahaneConst_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Kahane.html#TauCeti.rademacherMoment_le_kahaneConst_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.rademacherMoment_le_kahaneConst_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Kahane.html#TauCeti.rademacherMoment_le_kahaneConst_mul)
- [Source of `TauCeti.rademacherMoment_le_kahaneConst_mul` in TauCeti/Analysis/Normed/Module/RademacherSum/Kahane.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Kahane.lean#L289)
