# Profinite completion of the Hurwitz quaternions

We define $\widehat{\mathcal{O}}$ to be $\mathcal{O}\otimes\widehat{\mathbb{Z}}$, so it's elements $a+bi+cj+d\omega$ with $a,b,c,d\in\widehat{\mathbb{Z}}$. The basic thing we need is this:

- [Hurwitz.surjective\_pnat\_quotient](hurwitz-surjective-pnat-quotient.md)

We define $D:=\mathbb{Q}\otimes\mathcal{O}=\mathbb{Q}\oplus\mathbb{Q} i\oplus\mathbb{Q} j\oplus\mathbb{Q}\omega=\mathbb{Q}\oplus\mathbb{Q} i\oplus\mathbb{Q} j\oplus\mathbb{Q} k$. Finally, we define $\widehat{D}:=D\otimes\widehat{\mathbb{Z}}$. Just as with $\widehat{\mathbb{Q}}$ we have

- [HurwitzRatHat.canonicalForm](hurwitzrathat-canonicalform.md)

It is not hard to check that $\widehat{D}$ contains $\widehat{\mathcal{O}}$ and $D$ as subrings, and that as additive abelian groups we have $\widehat{\mathcal{O}}\cap D=\mathcal{O}$ and $\widehat{\mathcal{O}}+D=\widehat{D}$. This is because $\mathcal{O}$ is just four copies of $\mathbb{Z}$ and we've proved the analogous result for $\mathbb{Z}$.

However the multiplicative structure is more interesting, especially as $D$ is not commutative. For a general quaternion algebra it is *not* true that $(\widehat{D})^\times=D^\times(\widehat{\mathcal{O}})^\times$, because there are "class group obstructions". The double coset space is some kind of non-commutative analogue of a class group. However for our particular choice of $D$ and $\mathcal{O}$ the result is true.

- [HurwitzRatHat.completed\_units](hurwitzrathat-completed-units.md)
