%give credit to "xidui is very lazy" from github.io (https://xidui.github.io/)
%modify the funtion to help show the comparision between mongo and cassandra
function plot_result(size)
    file1 = strcat('mongo_result_',num2str(size),'.txt');
    file2 = strcat('casandra_result_',num2str(size),'.txt');
    mongo = load(file1);
    casandra = load(file2);
    data_size = mongo(:, 1);
    mongo_insert_vec = mongo(:, 2);
    casandra_insert_vec = casandra(:, 2);
    mongo_search_vec = mongo(:, 3);
    casandra_search_vec = casandra(:, 3);
    % insert
    plot(data_size, mongo_insert_vec);
    grid on;
    hold on;
    size = 1000;
    plot(data_size, casandra_insert_vec);
    title([num2str(size), 'w insert compare']);
    legend('mongodb', 'casandra');
    xlabel('data size');
    ylabel(strcat('insert time per',num2str(size), 'query'));
    saveas(gcf, ['insert_comp_', num2str(size), '.jpg'])
    hold off;

    plot(data_size, mongo_search_vec);
    grid on;
    hold on;
    plot(data_size, casandra_search_vec);
    title('QPS');
    title([num2str(size), 'w search compare']);
    legend('mongodb', 'casandra');
    xlabel('data size');
    ylabel(strcat('search time per',num2str(size), 'query'));
    saveas(gcf, ['search_comp_', num2str(size), '.jpg'])
    hold off;
end
