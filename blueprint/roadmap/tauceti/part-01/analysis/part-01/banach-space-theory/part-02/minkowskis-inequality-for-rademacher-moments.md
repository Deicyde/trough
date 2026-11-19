---
declaration: theorem
origin: cited
lean: TauCeti.rademacherMoment_add_le
statement: formalized
proof: formalized
---

# Minkowski's inequality for Rademacher moments

for `1 ≤ p`, `rademacherMoment p` is
subadditive.

```lean
TauCeti.rademacherMoment_add_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι] [DecidableEq ι]
  [SeminormedAddCommGroup E] {p : ℝ} (hp : 1 ≤ p) (y z : ι → E) :
  TauCeti.rademacherMoment p (y + z) ≤ TauCeti.rademacherMoment p y + TauCeti.rademacherMoment p z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.rademacherMoment_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Moment.html#TauCeti.rademacherMoment_add_le).

## Sources

- [Tau Ceti documentation: `TauCeti.rademacherMoment_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Moment.html#TauCeti.rademacherMoment_add_le)
- [Source of `TauCeti.rademacherMoment_add_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Moment.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Moment.lean#L349)
