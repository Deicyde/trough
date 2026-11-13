---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistCharacter, MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.theta, MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistedRightIdealsIntersect, MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistedRightIdealsIntersect_refuted
statement: formalized
---

# Right ideals of free group algebras

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html).

## Twisting character of the free group of rank two

Let $F$ be the free group on $x, y$. For
nonzero complex numbers $a, b$, this is the homomorphism $\chi \colon F \to \mathbb{C}^\times$ with
$\chi(x) = a$ and $\chi(y) = b$.

Formalized by `MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistCharacter`, a definition declared in [WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html#twist-character).

## Twisting automorphism of the free group algebra

Let $F$ be the free group on $x, y$, let
$\mathbb{C}F$ be its complex group algebra, and for nonzero complex numbers $a, b$ let $\chi$ be the
character of $F$ with $\chi(x) = a$ and $\chi(y) = b$. The map $\vartheta_{a,b}$ sends
$\alpha = \sum_{g \in F} c_g\, g \in \mathbb{C}F$ to $\sum_{g \in F} \chi(g)\, c_g\, g$.

Since $\chi$ is a homomorphism, $\vartheta_{a,b}$ is the algebra automorphism of $\mathbb{C}F$ with
$\vartheta_{a,b}(x) = a x$ and $\vartheta_{a,b}(y) = b y$.

Formalized by `MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.theta`, a definition declared in [WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html#theta).

## Linnell's twisted right ideal question (Kourovka 12.46)

Let $F$ be the free group on
$x, y$, let $\mathbb{C}F$ be its complex group algebra, and for nonzero complex numbers $a, b$ let
$\vartheta_{a,b}$ be the twisting automorphism of $\mathbb{C}F$ with $\vartheta_{a,b}(x) = a x$ and
$\vartheta_{a,b}(y) = b y$. The assertion is that for every nonzero $\alpha \in \mathbb{C}F$ there
are complex numbers $a, b \neq 1$ with $|a| = |b| = 1$ such that the right ideals
$\alpha\,\mathbb{C}F$ and $\vartheta_{a,b}(\alpha)\,\mathbb{C}F$ intersect nontrivially, that is,
$\alpha\beta = \vartheta_{a,b}(\alpha)\gamma \neq 0$ for some $\beta, \gamma \in \mathbb{C}F$.

Formalized by `MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistedRightIdealsIntersect`, a definition declared in [WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html#twisted-right-ideals-intersect).

## Linnell's twisted right ideal question has a negative answer (Kourovka 12.46)

Let $F$ be the
free group on $x, y$, let $\mathbb{C}F$ be its complex group algebra, and for nonzero complex
numbers $a, b$ let $\vartheta_{a,b}$ be the twisting automorphism of $\mathbb{C}F$ with
$\vartheta_{a,b}(x) = a x$ and $\vartheta_{a,b}(y) = b y$. There is a nonzero
$\alpha \in \mathbb{C}F$ such that for all complex numbers $a, b \neq 1$ with $|a| = |b| = 1$
the right ideals $\alpha\,\mathbb{C}F$ and $\vartheta_{a,b}(\alpha)\,\mathbb{C}F$ intersect only in
$0$: whenever $\beta, \gamma \in \mathbb{C}F$ satisfy $\alpha\beta = \vartheta_{a,b}(\alpha)\gamma$,
then $\alpha\beta = 0$.

The Kourovka Archive answers 12.46 "No, not always" (A. V. Tushev, 1995).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.46 (P. A. Linnell); resolution: A. V. Tushev, Ukrain. Mat. Zh. 47 (1995), no. 4, 571-572, Kourovka Archive, Problem 12.46: No, not always.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.twistedRightIdealsIntersect_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupAlgebraTwistedIdealsKourovka12Problem46Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html#twisted-right-ideals-intersect-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Right ideals of free group algebras](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/group-rings/right-ideals-of-free-group-algebras)
