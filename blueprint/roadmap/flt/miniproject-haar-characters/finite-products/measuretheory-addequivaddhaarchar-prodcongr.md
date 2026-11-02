---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_prodCongr
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/520
---

# MeasureTheory.addEquivAddHaarChar\_prodCongr

If $(A,+)$ and $(B,+)$ are locally compact topological abelian groups, and if $\phi:A\to A$ and $\psi:B\to B$ are additive homeomorphisms, then $\phi\times\psi:A\times B\to A\times B$ is an additive homeomorphism (this is obvious), and $d_{A\times B}(\phi\times\psi)=d_A(\phi)d_B(\psi)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We only need this result in the case where both $A$ and $B$ are second-countable, in which case Prod.borelSpace can be used to show that Haar measure on $A\times B$ is the product of Haar measures on $A$ and $B$, and in this case the result follows easily. Without this assumption, the product of these measures may not even be a Borel measure and one has to be more careful. The proof in this case is explained by Gouëzel [here](https://leanprover.zulipchat.com/#narrow/channel/116395-maths/topic/Product.20of.20Borel.20spaces/near/487257981). Here is the idea. Let $\rho$ be a Haar measure on $A\times B$. Fix sets $X\subseteq A$ and $Y\subseteq B$ which are compact with nonempty interior. We can now pull back $\rho$ to a measure $\nu$ on the Borel sigma-algebra of $A$ defined as $\nu(s)=\rho(s\times Y)$ and this is easily checked to be a Haar measure on $A$. Then $\delta_{A\times B}(a,0)\nu(X)= \delta_{A\times B}(a,0)\rho(X\times Y)=\rho((a,0)(X\times Y))= \rho(aX\times Y)=\nu(aX)=\delta_A(a)\nu(X)$ , so $\delta_{A\times B}(a,0)=\delta_A(a)$. Similarly $\delta_{A\times B}(0,b)=\delta_B(b)$ and because $\delta_{A\times B}$ is a group homomorphism we're home.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_prodCongr`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_prodCongr).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 456](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L456)
