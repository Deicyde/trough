---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_gelfandNaimark, MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_russoDye, MathlibExt.Analysis.CStarAlgebra.StinespringWanted.stinespring_dilation
statement: formalized
proof: formalized
---

# Banach and operator algebras: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/index.html).

Banach algebras and C*- and von Neumann algebras: exponentials and product formulas in Banach algebras, GNS, Gelfand–Naimark, bicommutant, Kaplansky density, Russo–Dye, Stinespring, Kadison–Singer and the Marcus–Spielman–Srivastava theorem.

## Gelfand–Naimark theorem

For every unital C*-algebra $A$ there are a complex Hilbert space $H$
and a unital $*$-homomorphism $\pi : A \to B(H)$ into the algebra of bounded operators on $H$ such
that $\pi$ is injective and isometric: $\|\pi(a)\| = \|a\|$ for every $a \in A$.

## Sources

- Gelfand–Naimark theorem, I. M. Gelfand–M. A. Naimark, Mat. Sb. 12 (1943); see Murphy, C*-Algebras and Operator Theory, A Course in Operator Theory; Lean is isometric injective star-homomorphism into B(H) form.

Formalized by `MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_gelfandNaimark`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/Landmark.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/Landmark.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/index.html#c-star-algebra-gelfand-naimark).

## Russo–Dye theorem

In a unital C*-algebra $A$, the norm closure of the convex hull of the
unitary elements of $A$ equals the closed unit ball $\{a \in A : \|a\| \le 1\}$.

## Sources

- Russo–Dye theorem, B. Russo–H. Dye, Duke Math. J. 33 (1966); see Takesaki I; Lean is norm-closure of convex hull of unitaries equals closed unit ball.

Formalized by `MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_russoDye`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/RussoDye.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/RussoDye.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/index.html#c-star-algebra-russo-dye).

## Stinespring dilation theorem

Let $A$ be a unital C*-algebra with its standard order, let $H$
be a complex Hilbert space, and let $\varphi : A \to B(H)$ be a completely positive map. Then
there are a complex Hilbert space $K$, a unital $*$-homomorphism $\pi : A \to B(K)$ and a bounded
linear map $V : H \to K$ such that $\varphi(a) = V^* \pi(a) V$ for every $a \in A$, where $V^*$
is the adjoint of $V$.

## Sources

- Stinespring dilation theorem, W. F. Stinespring, Proc. Amer. Math. Soc. 6 (1955); see Paulsen, Completely Bounded Maps; Lean is general CP map A →CP B(H) dilation V† π(a) V, not finite-dimensional Kraus form.

Formalized by `MathlibExt.Analysis.CStarAlgebra.StinespringWanted.stinespring_dilation`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/Stinespring.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/Stinespring.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/index.html#stinespring-dilation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banach and operator algebras](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras)
