---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.gibbsWeight, CondensedMatter.QuasiLocal.gibbsRoot, CondensedMatter.QuasiLocal.gibbsWeight_eq_root_mul, CondensedMatter.QuasiLocal.gibbsRoot_isHermitian, CondensedMatter.QuasiLocal.gibbsWeight_isHermitian, CondensedMatter.QuasiLocal.partition, CondensedMatter.QuasiLocal.partition_eq, CondensedMatter.QuasiLocal.gibbsRoot_ne_zero
statement: formalized
proof: formalized
---

# Gibbs weights and states of a finite-dimensional system

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.Gibbs`, [PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean): 22 declarations, 14 with a docstring.

> The Gibbs state of a Hermitian energy operator, and the canonical and grand canonical ensembles.

## i. Overview

> For a Hermitian matrix `h`, thought of as `β` times an energy, the *Gibbs weight* is `e^{-h}`,
> and the *Gibbs state* is `a ↦ tr(e^{-h} a) / tr(e^{-h})`. It is a state of the matrix algebra: it
> is normalized, Hermitian, and positive, because the weight is the square `r²` of the Hermitian
> matrix `r = e^{-h/2}`, so that `tr(r² a* a) = tr((a r)* (a r)) ≥ 0`, and the partition function
> `tr(r²)` is positive.
>
> Every ensemble is a special case.
>
> * The *canonical ensemble* at inverse temperature `β` for a Hamiltonian `H` has `h = β H`.
> * The *grand canonical ensemble* at inverse temperature `β` and chemical potential `μ`, for a
>   Hamiltonian `H` and a charge `N` such as the particle number, has `h = β (H - μ N)`.
>   When the charge is conserved, `H` and `N` commute and the weight factorizes as
>   `e^{-βH} e^{βμN}`: the canonical weight times a fugacity `e^{βμ}` per unit charge.
>
> No structure of the system enters, so the same definitions serve a finite region of any lattice,
> quantum or classical. A classical system is the case of diagonal matrices, where the Gibbs weight
> is the Boltzmann factor `e^{-E(c)}` of each configuration `c`.

## ii. Key results

> - `gibbsWeight` : the weight `e^{-h}`.
> - `gibbsState` : the Gibbs state of a Hermitian operator, as a state of the matrix algebra.
> - `canonicalState` : the canonical ensemble.
> - `grandCanonicalState` : the grand canonical ensemble.
> - `grandCanonicalWeight_of_commute` : factorization for a conserved charge.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 5.3.

## A. The Gibbs weight

**`CondensedMatter.QuasiLocal.gibbsWeight`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L77).

> The Gibbs weight `e^{-h}` of an energy operator `h`.

```lean
def gibbsWeight (h : Matrix n n ℂ) : Matrix n n ℂ
```

**`CondensedMatter.QuasiLocal.gibbsRoot`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L80).

> The square root `e^{-h/2}` of the Gibbs weight.

```lean
def gibbsRoot (h : Matrix n n ℂ) : Matrix n n ℂ
```

**`CondensedMatter.QuasiLocal.gibbsWeight_eq_root_mul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L82).

```lean
lemma gibbsWeight_eq_root_mul (h : Matrix n n ℂ) : gibbsWeight h = gibbsRoot h * gibbsRoot h
```

**`CondensedMatter.QuasiLocal.gibbsRoot_isHermitian`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L88).

```lean
lemma gibbsRoot_isHermitian {h : Matrix n n ℂ} (hh : h.IsHermitian) :
    (gibbsRoot h).IsHermitian
```

**`CondensedMatter.QuasiLocal.gibbsWeight_isHermitian`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L94).

```lean
lemma gibbsWeight_isHermitian {h : Matrix n n ℂ} (hh : h.IsHermitian) :
    (gibbsWeight h).IsHermitian
```

**`CondensedMatter.QuasiLocal.partition`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L101).

> The **partition function** `tr e^{-h}`.

```lean
def partition (h : Matrix n n ℂ) : ℂ
```

**`CondensedMatter.QuasiLocal.partition_eq`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L103).

```lean
lemma partition_eq (h : Matrix n n ℂ) (hh : h.IsHermitian) :
    partition h = ((gibbsRoot h)ᴴ * gibbsRoot h).trace
```

**`CondensedMatter.QuasiLocal.gibbsRoot_ne_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L107).

```lean
lemma gibbsRoot_ne_zero [Nonempty n] (h : Matrix n n ℂ) : gibbsRoot h ≠ 0
```

**`CondensedMatter.QuasiLocal.partition_pos`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L114).

> **The partition function of a Hermitian operator is positive.**

```lean
lemma partition_pos [Nonempty n] {h : Matrix n n ℂ} (hh : h.IsHermitian) : 0 < partition h
```

**`CondensedMatter.QuasiLocal.partition_ne_zero`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L121).

```lean
lemma partition_ne_zero [Nonempty n] {h : Matrix n n ℂ} (hh : h.IsHermitian) :
    partition h ≠ 0
```

## B. The Gibbs state

**`CondensedMatter.QuasiLocal.gibbsFunctional`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L127).

> The Gibbs functional `a ↦ tr(e^{-h} a) / tr(e^{-h})`.

```lean
def gibbsFunctional (h : Matrix n n ℂ) : Matrix n n ℂ →ₗ[ℂ] ℂ
```

**`CondensedMatter.QuasiLocal.gibbsFunctional_apply`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L130).

```lean
lemma gibbsFunctional_apply (h a : Matrix n n ℂ) :
    gibbsFunctional h a = (partition h)⁻¹ * (gibbsWeight h * a).trace
```

**`CondensedMatter.QuasiLocal.inv_partition_nonneg`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L134).

> The inverse of the partition function is a nonnegative real number.

```lean
lemma inv_partition_nonneg [Nonempty n] {h : Matrix n n ℂ} (hh : h.IsHermitian) :
    0 ≤ (partition h)⁻¹
```

**`CondensedMatter.QuasiLocal.gibbsState`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L145).

> **The Gibbs state of a Hermitian operator** is a state of the matrix algebra: normalized,
> Hermitian and positive.

```lean
def gibbsState [Nonempty n] (h : Matrix n n ℂ) (hh : h.IsHermitian) : AlgState (Matrix n n ℂ)
```

## C. The canonical and grand canonical ensembles

**`CondensedMatter.QuasiLocal.canonicalState`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L176).

> **The canonical ensemble** at inverse temperature `β` for a Hamiltonian `H`.

```lean
def canonicalState [Nonempty n] (β : ℝ) (H : Matrix n n ℂ) (hH : H.IsHermitian) :
    AlgState (Matrix n n ℂ)
```

**`CondensedMatter.QuasiLocal.grandCanonicalOp`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L183).

> The operator whose Gibbs weight is the grand canonical weight: `β (H - μ N)`.

```lean
def grandCanonicalOp (β μ : ℝ) (H N : Matrix n n ℂ) : Matrix n n ℂ
```

**`CondensedMatter.QuasiLocal.grandCanonicalOp_isHermitian`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L187).

```lean
lemma grandCanonicalOp_isHermitian {H N : Matrix n n ℂ} (hH : H.IsHermitian) (hN : N.IsHermitian)
    (β μ : ℝ) : (grandCanonicalOp β μ H N).IsHermitian
```

**`CondensedMatter.QuasiLocal.grandCanonicalState`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L195).

> **The grand canonical ensemble** at inverse temperature `β` and chemical potential `μ`, for a
> Hamiltonian `H` and a charge `N`.

```lean
def grandCanonicalState [Nonempty n] (β μ : ℝ) (H N : Matrix n n ℂ) (hH : H.IsHermitian)
    (hN : N.IsHermitian) : AlgState (Matrix n n ℂ)
```

**`CondensedMatter.QuasiLocal.grandCanonicalOp_zero`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L201).

> At zero chemical potential the grand canonical ensemble is the canonical one.

```lean
lemma grandCanonicalOp_zero (β : ℝ) (H N : Matrix n n ℂ) :
    grandCanonicalOp β 0 H N = (β : ℂ) • H
```

**`CondensedMatter.QuasiLocal.grandCanonicalWeight_of_commute`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L207).

> **Factorization for a conserved charge**: if `H` and `N` commute, the grand canonical weight is
> the canonical weight times the fugacity factor `e^{βμ N}`.

```lean
lemma grandCanonicalWeight_of_commute (β μ : ℝ) {H N : Matrix n n ℂ} (hc : Commute H N) :
    gibbsWeight (grandCanonicalOp β μ H N) =
      gibbsWeight ((β : ℂ) • H) * NormedSpace.exp (((β * μ : ℝ) : ℂ) • N)
```

## D. Classical systems

**`CondensedMatter.QuasiLocal.gibbsWeight_diagonal`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L222).

> **For a diagonal energy operator the Gibbs weight is the Boltzmann factor** `e^{-E(c)}` of each
> configuration `c`: the classical Gibbs distribution.

```lean
lemma gibbsWeight_diagonal (v : n → ℂ) :
    gibbsWeight (Matrix.diagonal v) = Matrix.diagonal fun c => Complex.exp (-v c)
```

**`CondensedMatter.QuasiLocal.partition_diagonal`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean#L231).

> The partition function of a diagonal energy operator is the sum of the Boltzmann factors.

```lean
lemma partition_diagonal (v : n → ℂ) : partition (Matrix.diagonal v) = ∑ c, Complex.exp (-v c)
```

## Depends on

- [The GNS representation of a state on a unital `*`-algebra](../../probabilistictheory/staralgebra/gns.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Gibbs.lean)
