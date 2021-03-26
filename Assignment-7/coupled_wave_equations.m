[T,E] = ode45('F',[0 0.1],[7565283.5547819445;1;1]);
plot(T,sqrt(conj(E(:,1)) .* E(:,1)))
hold on
plot(T,sqrt(conj(E(:,2)) .* E(:,2)))
plot(T,sqrt(conj(E(:,3)) .* E(:,3)))
xlabel('L / m')
ylabel('|E| / (V / m)')
legend('|E_p|','|E_s|','|E_i|')