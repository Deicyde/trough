---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.NumberField.weakBSD, WeierstrassCurve.Affine.NumberField.strongBSD, WeierstrassCurve.Affine.Rat.weakBSD, WeierstrassCurve.Affine.Rat.strongBSD
statement: formalized
---

# The Birch and Swinnerton-Dyer (BSD) Conjecture

> ## References
>
> - [The Clay Institute](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/),
>   official problem description by Andrew Wiles:
>   [claymath.org](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf)
> - [BSD1965] B. J. Birch and H. P. F. Swinnerton-Dyer. "Notes on elliptic curves. II."
>   Journal fur die reine und angewandte Mathematik 218 (1965), 79-108,
>   [doi](https://doi.org/10.1515/crll.1965.218.79)
> - [Tate1966] John Tate. "On the conjectures of Birch and Swinnerton-Dyer and a geometric analog."
>   Seminaire Bourbaki, Vol. 9, Exp. No. 306 (1966), 415-440,
>   [numdam](https://www.numdam.org/item/SB_1964-1966__9__415_0/)
> - [Gross2011] Benedict H. Gross. "Lectures on the conjecture of Birch and Swinnerton-Dyer."
>   Arithmetic of L-functions, IAS/Park City Math. Ser. 18, AMS (2011), 169-209,
>   [math.harvard.edu](https://people.math.harvard.edu/~gross/preprints/lectures-pcmi.pdf)
> - [Ang2025] David Kurniadi Angdinata. "L-functions of Dirichlet twists of elliptic curves:
>   computations and congruences." PhD thesis, University College London (2025),
>   [discovery.ucl.ac.uk](https://discovery.ucl.ac.uk/10223687/1/main-pages.pdf)
> - [Ada] Tom Adamczewski. "Autoformalized conjectures",
>   [Birch and Swinnerton-Dyer](https://tadamcz.com/autoformalization-results/#/p/wp-birch-and-swinnerton-dyer-conjecture)
> - [DD2010] Tim Dokchitser and Vladimir Dokchitser. "On the Birch-Swinnerton-Dyer quotients
>   modulo squares." Annals of Mathematics 172 (2010), 567-596, Conjecture 2.1,
>   [annals](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n1-p11-p.pdf)

*Quoted from [FormalConjectures/Millennium/BSD.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 1 API statement, counted here but not shown.

## `WeierstrassCurve.Affine.NumberField.weakBSD`

Open: stated without proof.

> The **weak Birch and Swinnerton-Dyer conjecture** ([DD2010], Conjecture 2.1 (1); the order
> statement on its own is [Tate1966], Conjecture (A)).

```lean
theorem weakBSD [E.IsElliptic] : WeakBSD E
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Millennium/BSD.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean#L91).

## `WeierstrassCurve.Affine.NumberField.strongBSD`

Open: stated without proof.

> The **strong Birch and Swinnerton-Dyer conjecture** ([DD2010], Conjecture 2.1).

```lean
theorem strongBSD [E.IsElliptic] : StrongBSD E
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Millennium/BSD.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean#L96).

## `WeierstrassCurve.Affine.Rat.weakBSD`

Open: stated without proof.

> The **weak Birch and Swinnerton-Dyer conjecture** over `ℚ`, a Clay Millennium Prize Problem.

```lean
theorem weakBSD : NumberField.WeakBSD E
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Millennium/BSD.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean#L113).

## `WeierstrassCurve.Affine.Rat.strongBSD`

Open: stated without proof.

> The **strong Birch and Swinnerton-Dyer conjecture** over `ℚ`.

```lean
theorem strongBSD : NumberField.StrongBSD E
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Millennium/BSD.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/BSD.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/BSD.lean)
- [The Clay Institute](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
