---
declaration: theorem
origin: cited
lean: AuslanderReiten.auslander_reiten, AuslanderReiten.auslander_reiten.variants.commutative, AuslanderReiten.auslander_reiten.variants.local_free, AuslanderReiten.auslander_reiten.variants.normal, AuslanderReiten.auslander_reiten.variants.regular_local
statement: formalized
---

# The Auslander-Reiten conjecture

> **Auslander-Reiten conjecture.** Let $\Lambda$ be an Artin algebra and let $M$ be a finitely
> generated $\Lambda$-module with $\operatorname{Ext}^i_\Lambda(M, M) = 0$ and
> $\operatorname{Ext}^i_\Lambda(M, \Lambda) = 0$ for all $i > 0$. Then $M$ is projective.
>
> An *Artin algebra* is a ring $\Lambda$ that is an algebra over a commutative Artinian ring $A$
> and is finitely generated as an $A$-module.
>
> Auslander and Reiten [AR75] derived this from the generalized Nakayama conjecture. The
> conjecture for Artin algebras is false: an internal OpenAI model gave an explicit counterexample
> in September 2026 [OAI26], a finite-dimensional algebra over the field
> $\mathbb{F}_2(q, H_1, H_2)$ with a finite-dimensional non-projective module satisfying both
> vanishing conditions. The commutative version, obtained by replacing $\Lambda$ with a
> commutative Noetherian ring $R$, is open and is what the commutative algebra literature calls
> the Auslander-Reiten conjecture. The two hypotheses are together equivalent to
> $\operatorname{Ext}^i_R(M, R \oplus M) = 0$ for all $i > 0$.
>
> Known cases of the commutative version include: $R$ a locally excellent Cohen-Macaulay normal
> ring containing $\mathbb Q$ [HL04]; $R$ a Gorenstein normal ring [Ar09]; $R$ a Cohen-Macaulay
> normal ring [KOT22]; and, most generally, $R$ any normal ring [Ki23]. Auslander, Ding and Solberg
> [ADS93] proved it for local complete intersections. The commutative version is open in general,
> already for commutative Noetherian local rings.
>
> *References:*
> - [AR75] M. Auslander, I. Reiten, *On a generalized version of the Nakayama conjecture*, Proc.
>   Amer. Math. Soc. 52 (1975), 69-74.
>   [PDF](https://www.ams.org/journals/proc/1975-052-01/S0002-9939-1975-0389977-6/S0002-9939-1975-0389977-6.pdf)
> - [Wikipedia, Nakayama conjecture](https://en.wikipedia.org/wiki/Nakayama_conjecture), on the
>   generalized Nakayama conjecture of [AR75].
> - [ADS93] M. Auslander, S. Ding, Ø. Solberg, *Liftings and weak liftings of modules*, J. Algebra
>   156 (1993), 273-317.
> - [HL04] C. Huneke, G. J. Leuschke, *On a conjecture of Auslander and Reiten*, J. Algebra 275
>   (2004), no. 2, 781-790. [arXiv:math/0305001](https://arxiv.org/abs/math/0305001)
> - [Ar09] T. Araya, *The Auslander-Reiten conjecture for Gorenstein rings*, Proc. Amer. Math. Soc.
>   137 (2009), 1941-1944.
> - [KOT22] K. Kimura, Y. Otake, R. Takahashi, *Maximal Cohen-Macaulay tensor products and
>   vanishing of Ext modules*, Bull. Lond. Math. Soc. 54 (2022), no. 6, 2456-2468.
> - [Ki23] K. Kimura, *Auslander-Reiten conjecture for normal rings*,
>   [arXiv:2304.03956](https://arxiv.org/abs/2304.03956). The statements of the conjecture
>   formalised below follow this paper.
> - [OAI26] OpenAI, *An explicit counterexample to the Auslander-Reiten conjecture*. OpenAI Math
>   Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Paper/AuslanderReiten.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `AuslanderReiten.auslander_reiten`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AuslanderReiten/All.lean#L738](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AuslanderReiten/All.lean#L738).

> **The Auslander-Reiten conjecture** [AR75] is false. The conjecture states: let $\Lambda$ be an
> Artin algebra and $M$ a finitely generated $\Lambda$-module with
> $\operatorname{Ext}^i_\Lambda(M, \Lambda) = 0$ and $\operatorname{Ext}^i_\Lambda(M, M) = 0$
> for all $i > 0$. Then $M$ is projective.
>
> That $\Lambda$ is an Artin algebra is the hypothesis that it is an algebra over some commutative
> Artinian ring `A` and is finitely generated as an `A`-module.
>
> This was disproved by an internal OpenAI model in September 2026 [OAI26]; see the linked Lean
> proof. The counterexample is a finite-dimensional algebra over the field
> $\mathbb{F}_2(q, H_1, H_2)$, which is the ring `A` there.

```lean
theorem auslander_reiten :
    ¬ ∀ (Λ : Type) [Ring Λ] (M : Type) [AddCommGroup M] [Module Λ M] [Module.Finite Λ M]
      (A : Type) [CommRing A] [IsArtinianRing A] [Algebra A Λ] [Module.Finite A Λ],
      (∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of Λ M) (ModuleCat.of Λ Λ) i)) →
      (∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of Λ M) (ModuleCat.of Λ M) i)) →
      Module.Projective Λ M
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [18 Category theory; homological algebra](../../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Paper/AuslanderReiten.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean#L109).

## `AuslanderReiten.auslander_reiten.variants.commutative`

Open: stated without proof.

> **The Auslander-Reiten conjecture for commutative Noetherian rings** [Ki23]. If $R$ is a
> commutative Noetherian ring and $M$ is a finitely generated $R$-module with
> $\operatorname{Ext}^i_R(M, R \oplus M) = 0$ for all $i > 0$, then $M$ is projective.

```lean
theorem auslander_reiten.variants.commutative
    (hMR : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R R) i))
    (hMM : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R M) i)) :
    Module.Projective R M
```

Category `research open`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [18 Category theory; homological algebra](../../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Paper/AuslanderReiten.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean#L130).

## `AuslanderReiten.auslander_reiten.variants.local_free`

Open: stated without proof.

> Over a Noetherian local ring a finitely generated projective module is free, so the conjecture
> takes the following form there. It is open in this case too.

```lean
theorem auslander_reiten.variants.local_free [IsLocalRing R]
    (hMR : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R R) i))
    (hMM : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R M) i)) :
    Module.Free R M
```

Category `research open`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [18 Category theory; homological algebra](../../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Paper/AuslanderReiten.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean#L141).

## `AuslanderReiten.auslander_reiten.variants.normal`

Solved: stated here without proof.

> The conjecture holds for normal rings [Ki23, Corollary 1.2]. Stated here for normal domains,
> since Mathlib does not currently have a standalone class for normal rings, which are the rings
> whose localizations at all primes are normal domains.

```lean
theorem auslander_reiten.variants.normal [IsDomain R] [IsIntegrallyClosed R]
    (hMR : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R R) i))
    (hMM : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R M) i)) :
    Module.Projective R M
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [18 Category theory; homological algebra](../../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Paper/AuslanderReiten.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean#L153).

## `AuslanderReiten.auslander_reiten.variants.regular_local`

Textbook result, stated without proof.

> Over a regular local ring the conjecture is standard: every finitely generated module has finite
> projective dimension $p$, and if $p > 0$ then $\operatorname{Ext}^p_R(M, R) \ne 0$. Only the
> vanishing of $\operatorname{Ext}^i_R(M, R)$ is used, and the conclusion is freeness.

```lean
theorem auslander_reiten.variants.regular_local [IsRegularLocalRing R]
    (hMR : ∀ i > 0, Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R R) i)) :
    Module.Free R M
```

Category `textbook`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [18 Category theory; homological algebra](../../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Paper/AuslanderReiten.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean#L166).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/AuslanderReiten.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/AuslanderReiten.lean)
- [PDF](https://www.ams.org/journals/proc/1975-052-01/S0002-9939-1975-0389977-6/S0002-9939-1975-0389977-6.pdf)
