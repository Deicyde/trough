---
declaration: theorem
origin: cited
lean: SerreUniformity.serre_uniformity, SerreUniformity.serre_uniformity.variants.bound_37
statement: formalized
---

# Serre's uniformity conjecture over the rationals

> Is there a bound $C$, independent of the non-CM elliptic curve $E/\mathbb{Q}$, such that
> the Galois action on $E[p]$ is surjective onto $\mathrm{GL}_2(\mathbb{F}_p)$ for every
> prime $p > C$? This is the $\mathbb{Q}$ case of Serre's question [Ser72], recalled in
> the introduction of [Lem17].
>
> We express surjectivity without choosing a basis: every additive automorphism of $E[p]$
> must be induced by an element of $G_{\mathbb{Q}}$. For prime $p$, these automorphisms are
> exactly the $\mathbb{F}_p$-linear automorphisms. The non-CM condition uses the classification
> of rational CM $j$-invariants.
>
> *References:*
> - [Ser72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes
>   elliptiques*. Inventiones Mathematicae 15 (1972), 259–331.
>   https://doi.org/10.1007/BF01405086
> - [Lem17] P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational
>   cyclic isogenies*, introduction. https://arxiv.org/abs/1702.01985

*Quoted from [FormalConjectures/Paper/SerreUniformity.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/SerreUniformity.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `SerreUniformity.serre_uniformity`

Open: stated without proof.

> **Serre's uniformity question over $\mathbb{Q}$** [Ser72, Lem17]: is there a bound
> $C$ such that every non-CM elliptic curve over $\mathbb{Q}$ has surjective mod-$p$
> Galois representation for every prime $p > C$?

```lean
theorem serre_uniformity :
    ∃ C : ℕ, ∀ (E : WeierstrassCurve ℚ) [E.IsElliptic], E.j ∉ cmJInvariants →
      ∀ p : ℕ, p.Prime → C < p → HasFullTorsionAction E p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/SerreUniformity.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/SerreUniformity.lean#L68).

## `SerreUniformity.serre_uniformity.variants.bound_37`

Open: stated without proof.

> **Serre's uniformity conjecture over $\mathbb{Q}$, explicit form**: the bound $C = 37$
> works, i.e. every non-CM elliptic curve over $\mathbb{Q}$ has surjective mod-$p$ Galois
> representation for every prime $p > 37$. From the introduction of [Lem17]: "This conjecture
> remains open today, but, over the last forty years, there has been a lot of progress towards
> a proof for $K = \mathbb{Q}$ — it is believed that, in this case, $p_K = 37$."

```lean
theorem serre_uniformity.variants.bound_37 :
    ∀ (E : WeierstrassCurve ℚ) [E.IsElliptic], E.j ∉ cmJInvariants →
      ∀ p : ℕ, p.Prime → 37 < p → HasFullTorsionAction E p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/SerreUniformity.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/SerreUniformity.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/SerreUniformity.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/SerreUniformity.lean)
- [https://doi.org/10.1007/BF01405086](https://doi.org/10.1007/BF01405086)
