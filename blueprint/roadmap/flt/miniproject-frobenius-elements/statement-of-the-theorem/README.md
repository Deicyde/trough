# Statement of the theorem

The set-up throughout this project: $G$ is a finite group acting (via ring isomorphisms) on a commutative ring $B$, and $A$ is the subring of $G$-invariants.

Say $Q$ is a prime ideal of $B$, whose pullback to $A$ is the prime ideal $P$. Note that $G$ naturally acts on the ideals of $B$. Let's define the *decomposition group* $D_Q$ of $Q$ to be the subgroup of $G$ which stabilizes $Q$ (just to be clear: $g\in D_Q$ means $\{g\cdot q\, :\, q \in Q\}=Q$, not $\forall q\in Q, g\cdot q=q$).

Let $L$ be the field of fractions of the integral domain $B/Q$, and let $K$ be the field of fractions of the subring $A/P$. Then $L$ is naturally a $K$-algebra. In this generality $L/K$ may not even be finite or Galois, but we can still talk about $\operatorname{Aut}(L/K)$.

In the next definition we write down a group homomorphism $\phi$ from $D_Q$ to $\operatorname{Aut}(L/K)$.

- [IsFractionRing.stabilizerHom](isfractionring-stabilizerhom.md)
- [IsFractionRing.stabilizerHom\_surjective](isfractionring-stabilizerhom-surjective.md)
