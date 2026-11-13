---
declaration: module
origin: cited
lean: PureU1.PureU1Charges, PureU1.accGrav, PureU1.accCubeTriLinSymm, PureU1.accCube, PureU1.accCube_explicit, PureU1, pureU1EqCharges, pureU1_linear
statement: formalized
proof: formalized
---

# Anomaly cancellation of a theory with a pure U(1)-gauge group

The module `Physlib.QFT.QED.AnomalyCancellation.Basic`, [Physlib/QFT/QED/AnomalyCancellation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean): 13 declarations, 13 with a docstring.

> In a pure U(1) gauge theory with `n` Weyl fermions carrying charges `xᵢ` the anomaly cancellation
> conditions (ACCs) which must be satisfied for a consistent gauge theory correspond to:
>
> - The linear ACC: `∑ xᵢ = 0`
> - The cubic ACC: `∑ xᵢ³ = 0`
>
> The charges `xᵢ` have rational fractions with one another, here they are specified as
> rational numbers.

**`PureU1.PureU1Charges`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L41).

> The vector space of charges.

```lean
def PureU1Charges (n : ℕ) : ACCSystemCharges
```

**`PureU1.accGrav`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L46).

> The gravitational anomaly.

```lean
def accGrav (n : ℕ) : ((PureU1Charges n).Charges →ₗ[ℚ] ℚ)
```

**`PureU1.accCubeTriLinSymm`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L56).

> The symmetric trilinear form used to define the cubic anomaly.

```lean
def accCubeTriLinSymm {n : ℕ} : TriLinearSymm (PureU1Charges n).Charges
```

**`PureU1.accCube`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L85).

> The cubic anomaly equation.

```lean
def accCube (n : ℕ) : HomogeneousCubic ((PureU1Charges n).Charges)
```

**`PureU1.accCube_explicit`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L90).

> The cubic ACC for the pure-`U(1)` anomaly equations is equal to the sum of the cubed
> charges.

```lean
lemma accCube_explicit (n : ℕ) (S : (PureU1Charges n).Charges) :
    accCube n S = ∑ i : Fin n, S i ^ 3
```

**`PureU1`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L102).

> The ACC system for a pure $U(1)$ gauge theory with $n$ fermions.

```lean
def PureU1 (n : ℕ) : ACCSystem
```

**`pureU1EqCharges`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L113).

> An equivalence of vector spaces of charges when the number of fermions is equal.

```lean
def pureU1EqCharges {n m : ℕ} (h : n = m) :
    (PureU1 n).Charges ≃ₗ[ℚ] (PureU1 m).Charges
```

**`pureU1_linear`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L126).

> A solution to the pure U(1) accs satisfies the linear ACCs.

```lean
lemma pureU1_linear {n : ℕ} (S : (PureU1 n).LinSols) :
    ∑ (i : Fin n), S.val i = 0
```

**`pureU1_cube`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L134).

> A solution to the pure U(1) accs satisfies the cubic ACCs.

```lean
lemma pureU1_cube {n : ℕ} (S : (PureU1 n).Sols) :
    ∑ i, (S.val i) ^ 3 = 0
```

**`pureU1_last`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L142).

> The last charge of a solution to the linear ACCs is equal to the negation of the sum
> of the other charges.

```lean
lemma pureU1_last {n : ℕ} (S : (PureU1 n.succ).LinSols) :
    S.val (Fin.last n) = - ∑ i : Fin n, S.val i.castSucc
```

**`pureU1_anomalyFree_ext`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L151).

> Two solutions to the Linear ACCs for `n.succ` are equal if their first `n` charges are
> equal.

```lean
lemma pureU1_anomalyFree_ext {n : ℕ} {S T : (PureU1 n.succ).LinSols}
    (h : ∀ (i : Fin n), S.val i.castSucc = T.val i.castSucc) : S = T
```

**`PureU1.sum_of_charges`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L166).

> The `j`th charge of a sum of pure-`U(1)` charges is equal to the sum of
> their `j`th charges.

```lean
lemma sum_of_charges {n : ℕ} (f : Fin k → (PureU1 n).Charges) (j : Fin n) :
    (∑ i : Fin k, (f i)) j = ∑ i : Fin k, (f i) j
```

**`PureU1.sum_of_anomaly_free_linear`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean#L179).

> The `j`th charge of a sum of solutions to the linear ACC is equal to the sum of
> their `j`th charges.

```lean
lemma sum_of_anomaly_free_linear {n : ℕ} (f : Fin k → (PureU1 n).LinSols) (j : Fin n) :
    (∑ i : Fin k, (f i)).1 j = (∑ i : Fin k, (f i).1 j)
```

## Depends on

- [Anomaly cancellation conditions](../anomalycancellation/basic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Basic.lean)
