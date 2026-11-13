---
declaration: section
origin: cited
lean: RealGalois.finrank_eq_one_or_two, RealGalois.gal_card_eq_one_or_two, RealGalois.gal_card_pow_two
statement: formalized
proof: formalized
---

# Galois extensions of the real numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers/index.html).

## Degree of a finite extension of the reals

If $E$ is a field that is a finite-dimensional
algebra over $\mathbb{R}$, then the dimension of $E$ as a real vector space is $1$ or $2$.

This follows because such a field $E$ is isomorphic as an $\mathbb{R}$-algebra to $\mathbb{R}$ or
to $\mathbb{C}$.

Formalized by `RealGalois.finrank_eq_one_or_two`, a theorem declared in [MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers/index.html#finrank-eq-one-or-two).

## Galois groups over the reals have order 1 or 2

If $E$ is a finite Galois extension of
$\mathbb{R}$, then the Galois group $\mathrm{Gal}(E/\mathbb{R})$ has order $1$ or $2$.

Formalized by `RealGalois.gal_card_eq_one_or_two`, a theorem declared in [MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers/index.html#gal-card-eq-one-or-two).

## Galois groups over the reals have order a power of 2

If $E$ is a finite Galois extension
of $\mathbb{R}$, then the Galois group $\mathrm{Gal}(E/\mathbb{R})$ has order $2^n$ for some natural
number $n$.

In fact the order is $1$ or $2$.

## Sources

- the book's lemma in Lecture 34 (Main Theorem of Algebra).

Formalized by `RealGalois.gal_card_pow_two`, a theorem declared in [MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/GaloisGroupOverReal.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers/index.html#gal-card-pow-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Galois extensions of the real numbers](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/galois-theory/galois-extensions-of-the-real-numbers)
