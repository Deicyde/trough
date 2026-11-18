---
declaration: module
origin: cited
lean: SM.SMNoGrav.One.accGravSatisfied, SM.SMNoGrav.One.E_zero_iff_Q_zero, SM.SMNoGrav.One.accGrav_Q_zero, SM.SMNoGrav.One.accGrav_Q_ne_zero
statement: formalized
proof: formalized
---

# Lemmas for 1 family SM Accs

The module `Physlib.Particles.StandardModel.AnomalyCancellation.NoGrav.One.Lemmas`, [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean): 4 declarations, 4 with a docstring, 1 listed as significant.

> The main result of this file is the conclusion of this paper:
>   [Lohitsiri and Tong][Lohitsiri:2019fuu] [ref: Lohitsiri:2019fuu]
>
> That every solution to the ACCs without gravity satisfies for free the gravitational anomaly.

## References

> * The main result of this file is the conclusion of this paper. [ref: Lohitsiri:2019fuu]

**`SM.SMNoGrav.One.E_zero_iff_Q_zero`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean#L34).

> For a set of 1 family SM charges satisfying all ACCs except the gravitational,
> the charge of `Q` is zero if and only if `E` is zero.

```lean
lemma E_zero_iff_Q_zero {S : (SMNoGrav 1).Sols} : Q S.val (0 : Fin 1) = 0 ↔
    E S.val (0 : Fin 1) = 0
```

**`SM.SMNoGrav.One.accGrav_Q_zero`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean#L45).

> For a set of 1-family SM charges satisfying all ACCs except the gravitational,
> if the `Q` charge is zero then the charges satisfy the gravitational ACCs.

```lean
lemma accGrav_Q_zero {S : (SMNoGrav 1).Sols} (hQ : Q S.val (0 : Fin 1) = 0) :
    accGrav S.val = 0
```

**`SM.SMNoGrav.One.accGrav_Q_ne_zero`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean#L59).

> For a set of 1-family SM charges satisfying all ACCs except the gravitational,
> if the `Q` charge is not zero then the charges satisfy the gravitational ACCs.

```lean
lemma accGrav_Q_ne_zero {S : (SMNoGrav 1).Sols} (hQ : Q S.val (0 : Fin 1) ≠ 0) :
    accGrav S.val = 0
```

**`SM.SMNoGrav.One.accGravSatisfied`**, a theorem, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean#L71). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Any solution to the 1-family ACCs without gravity satisfies the gravitational ACC.

```lean
theorem accGravSatisfied {S : (SMNoGrav 1).Sols} :
    accGrav S.val = 0
```

## Depends on

- [Anomaly Cancellation in the Standard Model without Gravity](anomalycancellation-nograv-basic.md)

## Proof depends on

- [Parameterizations for solutions to the linear ACCs for 1 family](anomalycancellation-nograv-one-linearparameteriz.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/Lemmas.lean)
