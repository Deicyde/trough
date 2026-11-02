# A quaternion algebra

Let's define $D$ to be the quaternion algebra $\mathbb{Q}\oplus\mathbb{Q} i\oplus\mathbb{Q} j\oplus\mathbb{Q} k$. As a vector space, $D$ is 4-dimensional over $\mathbb{Q}$ with $[1,i,j,k]$ giving a basis. It has a (non-commutative)ring structure, with multiplication satisfying the usual quaternion algebra relations $i^2=j^2=k^2=ijk=-1$. You can think of $D$ as an analogue of $2\times 2$ matrices with rational coefficients, hence its units $D^\times$ are an analogue of the group $\operatorname{GL}_2(\mathbb{Q})$.

We will also need an analogue of the group $\operatorname{GL}_2(\mathbb{Z})$, which will come from an integral structure on $D$. We choose the Hurwitz order, namely the subring $\mathcal{O}:=\mathbb{Z}\oplus\mathbb{Z} i\oplus\mathbb{Z} j\oplus\mathbb{Z} \omega$, where $\omega=\frac{-1+(i+j+k)}{2}$, a cube root of unity, as $(i+j+k)^2=-3$. The simplest way to understand $\mathcal{O}$ is that it's quaternions $a+bi+cj+dk$ where either $a,b,c,d$ are all integers or are all in $\frac{1}{2}+\mathbb{Z}$.

Note that $\mathcal{O}$ is a maximal order and a Euclidean domain, which is why we prefer it over the more obvious sublattice $\mathbb{Z}\oplus\mathbb{Z} i\oplus\mathbb{Z} j\oplus\mathbb{Z} k.$

In this chapter, we are going to compute a complex vector space which could be called something like the “weight 2 level 2 modular forms for $D^\times$”. The main result will be that this space is 1-dimensional.

Note that mathlib has modular forms, but it doesn't have enough complex analysis to deduce that the space of modular forms of a given weight and level is finite-dimensional. If all the ‘sorry‘s in this chapter are completed before mathlib gets the necessary complex analysis, then the first nonzero space of modular forms to be proved finite-dimensional in Lean will be a space of quaternionic modular forms.

We will use a modern "adelic" definition of our modular forms, so the first thing we need to do is to talk about profinite completions.
